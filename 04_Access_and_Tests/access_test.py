#!/usr/bin/env python3
"""
NileCart Egypt - Access Control Test Script (fictional data only)
Standard library only.

Usage:
    python3 access_test.py              # run tests + mutation check, print tables
    python3 access_test.py --markdown   # also print a Markdown table for 08_Access_Control.md

How it maps to the authorization architecture (PAP / PIP / PDP / PEP):
    PAP  = ROLE_PERMISSIONS + the three rule functions   (where policy is written)
    PIP  = ACCOUNTS, REFUNDS, CHANGE_TICKETS             (where attributes are looked up)
    PDP  = decide()                                      (evaluates policy against attributes)
    PEP  = pep()                                         (enforces the decision, writes audit log)

IMPORTANT: decide() never sees a test ID or the expected result. "Actual" in the
output is computed purely from the request + the attributes + the rules. The
expected values are written by hand in TESTS, independently of the code.
The mutation check at the end proves every rule condition is really exercised:
if you switch a condition off, at least one test must fail.
"""

import sys

# ---------------------------------------------------------------- PAP: policy
# RBAC part: which role may perform which action on which resource.
ROLE_PERMISSIONS = {
    "Customer Support": {"order_file": {"read"}, "refunds": {"request"}},
    "Warehouse Staff":  {"order_file": {"read"}, "inventory": {"update"}},
    "Finance Officer":  {"order_file": {"read"}, "refunds": {"approve"},
                         "payment_reports": {"read"}},
    "IT Administrator": {"admin_settings": {"configure"}},
}


def _evaluate(rule_name, conditions, off):
    """Combine named conditions with AND. A condition listed in `off`
    (as 'rule:condition') is forced True - used only by the mutation check."""
    effective = {}
    for name, value in conditions.items():
        effective[name] = True if f"{rule_name}:{name}" in off else bool(value)
    return all(effective.values()), effective


def _has_permission(account, resource, action):
    return action in ROLE_PERMISSIONS.get(account["role"], {}).get(resource, set())


def rule1_read_order(account, req, off):
    """Rule 1: ALLOW = account_active AND correct_role AND object_assigned"""
    return _evaluate("rule1", {
        "account_active": account["active"],
        "correct_role": _has_permission(account, "order_file", "read"),
        "object_assigned": req["object"] in account["assigned"],
    }, off)


def rule2_refund_approve(account, req, off):
    """Rule 2: ALLOW = account_active AND correct_role AND mfa_verified
                       AND approver != requester   (segregation of duties)"""
    refund = REFUNDS.get(req["object"], {})
    return _evaluate("rule2", {
        "account_active": account["active"],
        "correct_role": _has_permission(account, "refunds", "approve"),
        "mfa_verified": account["mfa"],
        "approver_not_requester": refund.get("requester") not in (None, req["account"]),
    }, off)


def rule3_admin_config(account, req, off):
    """Rule 3: ALLOW = account_active AND correct_role AND mfa_verified
                       AND change_ticket_approved"""
    return _evaluate("rule3", {
        "account_active": account["active"],
        "correct_role": _has_permission(account, "admin_settings", "configure"),
        "mfa_verified": account["mfa"],
        "change_ticket_approved": CHANGE_TICKETS.get(req["object"], {}).get("approved", False),
    }, off)


def rbac_base(account, req, off):
    """Base RBAC check for everything else (e.g. inventory update):
       ALLOW = account_active AND correct_role"""
    return _evaluate("rbac", {
        "account_active": account["active"],
        "correct_role": _has_permission(account, req["resource"], req["action"]),
    }, off)


# Which rule governs which (resource, action). Anything else -> base RBAC check.
ROUTES = {
    ("order_file", "read"): ("Rule 1", rule1_read_order),
    ("refunds", "approve"): ("Rule 2", rule2_refund_approve),
    ("admin_settings", "configure"): ("Rule 3", rule3_admin_config),
}

# ---------------------------------------------------------------- PIP: attributes (fictional)
ACCOUNTS = {
    "sup-01":    {"role": "Customer Support", "active": True,  "mfa": True,  "assigned": {"ORD-1001"}},
    "sup-02":    {"role": "Customer Support", "active": True,  "mfa": True,  "assigned": {"ORD-1002"}},
    "sup-03":    {"role": "Customer Support", "active": False, "mfa": True,  "assigned": {"ORD-1001"}},
    "wh-01":     {"role": "Warehouse Staff",  "active": True,  "mfa": True,  "assigned": {"ORD-1001"}},
    "wh-03":     {"role": "Warehouse Staff",  "active": False, "mfa": True,  "assigned": set()},
    "fin-01":    {"role": "Finance Officer",  "active": True,  "mfa": True,  "assigned": set()},
    "fin-02":    {"role": "Finance Officer",  "active": True,  "mfa": True,  "assigned": set()},
    "fin-03":    {"role": "Finance Officer",  "active": True,  "mfa": False, "assigned": set()},
    "fin-04":    {"role": "Finance Officer",  "active": False, "mfa": True,  "assigned": set()},
    "it-01":     {"role": "IT Administrator", "active": True,  "mfa": True,  "assigned": {"ORD-1001"}},
    "it-02":     {"role": "IT Administrator", "active": True,  "mfa": False, "assigned": set()},
    "it-03":     {"role": "IT Administrator", "active": False, "mfa": True,  "assigned": set()},
    "orphan-01": {"role": None,               "active": True,  "mfa": True,  "assigned": {"ORD-1001"}},
}
REFUNDS = {"RF-1001": {"requester": "sup-01"}, "RF-1002": {"requester": "fin-01"}}
CHANGE_TICKETS = {"CHG-100": {"approved": True}, "CHG-101": {"approved": False}}


# ---------------------------------------------------------------- PDP
def decide(req, off=frozenset()):
    """Return (decision, rule_label, failed_conditions). Uses only req + PIP + PAP."""
    account = ACCOUNTS.get(req["account"])
    if account is None:
        return "DENY", "N/A", ["unknown_account"]
    label, rule = ROUTES.get((req["resource"], req["action"]), ("RBAC", rbac_base))
    ok, conds = rule(account, req, off)
    failed = [name for name, value in conds.items() if not value]
    return ("ALLOW" if ok else "DENY"), label, failed


# ---------------------------------------------------------------- PEP
AUDIT_LOG = []


def pep(req):
    """Enforce the PDP decision and record it (this is the 'gate' in front of the resource)."""
    decision, label, failed = decide(req)
    AUDIT_LOG.append((req["account"], req["resource"], req["action"], req["object"], decision))
    return decision, label, failed


# ---------------------------------------------------------------- tests
# (id, description, request, expected, related risk). Expected values are hand-written.
def R(account, resource, action, obj):
    return {"account": account, "resource": resource, "action": action, "object": obj}


TESTS = [
    ("T1",  "Support reads an order assigned to them",          R("sup-01", "order_file", "read", "ORD-1001"), "ALLOW", "R1/R2"),
    ("T2",  "Support reads an order NOT assigned to them",      R("sup-02", "order_file", "read", "ORD-1001"), "DENY",  "R2"),
    ("T3",  "Inactive (leaver) support account reads order",    R("sup-03", "order_file", "read", "ORD-1001"), "DENY",  "R1"),
    ("T4",  "Warehouse staff tries to approve a refund",        R("wh-01", "refunds", "approve", "RF-1001"),   "DENY",  "R5"),
    ("T5",  "Finance approves a refund they requested",         R("fin-01", "refunds", "approve", "RF-1002"),  "DENY",  "R5"),
    ("T6",  "Warehouse staff updates inventory",                R("wh-01", "inventory", "update", "INV-55"),   "ALLOW", "R4"),
    ("T7",  "Account with no role reads an assigned order",     R("orphan-01", "order_file", "read", "ORD-1001"), "DENY", "R1"),
    ("T8",  "IT admin changes settings, ticket NOT approved",   R("it-01", "admin_settings", "configure", "CHG-101"), "DENY", "R3"),
    ("T9",  "Finance (other person) approves a refund",         R("fin-02", "refunds", "approve", "RF-1001"),  "ALLOW", "R5"),
    ("T10", "Finance without MFA approves a refund",            R("fin-03", "refunds", "approve", "RF-1001"),  "DENY",  "R1/R5"),
    ("T11", "IT admin changes settings with approved ticket",   R("it-01", "admin_settings", "configure", "CHG-100"), "ALLOW", "R3"),
    ("T12", "IT admin without MFA changes settings",            R("it-02", "admin_settings", "configure", "CHG-100"), "DENY", "R1/R3"),
    ("T13", "IT admin reads an order (even if assigned)",       R("it-01", "order_file", "read", "ORD-1001"),  "DENY",  "R2"),
    ("T14", "Support tries to update inventory",                R("sup-01", "inventory", "update", "INV-55"),  "DENY",  "R4"),
    ("T15", "Inactive finance account approves a refund",       R("fin-04", "refunds", "approve", "RF-1001"),  "DENY",  "R1/R5"),
    ("T16", "Inactive IT admin changes settings",               R("it-03", "admin_settings", "configure", "CHG-100"), "DENY", "R1/R3"),
    ("T17", "Finance officer changes admin settings",           R("fin-02", "admin_settings", "configure", "CHG-100"), "DENY", "R3"),
    ("T18", "Inactive warehouse account updates inventory",     R("wh-03", "inventory", "update", "INV-55"),   "DENY",  "R4"),
    ("T19", "Unknown account reads an order",                   R("ghost-99", "order_file", "read", "ORD-1001"), "DENY", "R1"),
]


def run_tests(off=frozenset(), quiet=False):
    rows, failed = [], 0
    for tid, desc, req, expected, risk in TESTS:
        actual, label, why = decide(req, off) if off else pep(req)
        result = "PASS" if actual == expected else "FAIL"
        failed += result == "FAIL"
        rows.append((tid, desc, req, label, expected, actual, result, risk, why))
    if not quiet:
        print_table(rows)
    return rows, failed


def print_table(rows):
    line = "=" * 132
    print(line)
    print(f"{'ID':<4} | {'Account':<9} | {'Resource/Action':<24} | {'Rule':<7} | "
          f"{'Expected':<8} | {'Actual':<6} | {'Result':<6} | {'Risk':<6} | Failed condition(s)")
    print("-" * 132)
    for tid, _, req, label, exp, act, res, risk, why in rows:
        ra = f"{req['resource']}/{req['action']}"
        print(f"{tid:<4} | {req['account']:<9} | {ra:<24} | {label:<7} | "
              f"{exp:<8} | {act:<6} | {res:<6} | {risk:<6} | {', '.join(why) or '-'}")
    print(line)


def print_markdown(rows):
    print("\n| Test | Scenario | Account | Resource / Action | Rule | Expected | Actual | Pass/Fail | Risk | Why denied |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for tid, desc, req, label, exp, act, res, risk, why in rows:
        print(f"| {tid} | {desc} | {req['account']} | {req['resource']} / {req['action']} | "
              f"{label} | {exp} | {act} | {res} | {risk} | {', '.join(why) or '-'} |")


def mutation_check():
    """Switch each rule condition off, one at a time. A good test suite must then FAIL at least once."""
    mutants = [
        "rule1:account_active", "rule1:correct_role", "rule1:object_assigned",
        "rule2:account_active", "rule2:correct_role", "rule2:mfa_verified", "rule2:approver_not_requester",
        "rule3:account_active", "rule3:correct_role", "rule3:mfa_verified", "rule3:change_ticket_approved",
        "rbac:account_active", "rbac:correct_role",
    ]
    print("\nMutation check (each condition disabled -> at least one test must FAIL):")
    survivors = []
    for m in mutants:
        _, failed = run_tests(off=frozenset({m}), quiet=True)
        status = f"caught by {failed} test(s)" if failed else "NOT CAUGHT"
        if not failed:
            survivors.append(m)
        print(f"  {m:<32} -> {status}")
    return survivors


def main():
    rows, failed = run_tests()
    allow = sum(1 for r in rows if r[4] == "ALLOW")
    print(f"Summary: {len(rows) - failed} passed, {failed} failed out of {len(rows)} tests "
          f"({allow} ALLOW cases, {len(rows) - allow} DENY cases).")
    print(f"PEP audit log entries written: {len(AUDIT_LOG)}")
    if "--markdown" in sys.argv:
        print_markdown(rows)
    survivors = mutation_check()
    if survivors:
        print(f"\nWARNING: {len(survivors)} condition(s) are not covered by any test: {survivors}")
    ok = failed == 0 and not survivors
    print("\nOVERALL:", "ALL CHECKS PASSED" if ok else "PROBLEMS FOUND")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()