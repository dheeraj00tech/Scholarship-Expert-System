"""Inference engine for the Smart Scholarship Eligibility System.

Expert system parts:
  Knowledge base   -> scholarships.json (the rules)
  Inference engine -> evaluate_all() below
  Explanation      -> each result lists rules passed and failed
"""
import json
from pathlib import Path

KB_PATH = Path(__file__).parent / "scholarships.json"


def load_knowledge_base(path=KB_PATH):
    with open(path, encoding="utf-8") as f:
        return json.load(f)["scholarships"]


def check_rule(rule, facts):
    """Return True if a single rule is satisfied by the student's facts."""
    actual = facts.get(rule["field"])
    op, expected = rule["op"], rule["value"]
    if op == "in":
        return actual in expected
    if op == "==":
        return actual == expected
    if op == "<=":
        return actual <= expected
    if op == ">=":
        return actual >= expected
    raise ValueError(f"Unknown operator: {op}")


def evaluate_scholarship(scholarship, facts):
    passed, failed = [], []
    for rule in scholarship["rules"]:
        (passed if check_rule(rule, facts) else failed).append(rule["label"])
    return {
        "name": scholarship["name"],
        "provider": scholarship["provider"],
        "benefit": scholarship["benefit"],
        "priority": scholarship["priority"],
        "eligible": not failed,
        "passed": passed,
        "failed": failed,
        "match_percent": round(100 * len(passed) / len(scholarship["rules"])),
    }


def evaluate_all(facts, scholarships=None):
    """Forward chaining: fire every rule set against the facts.

    Returns (eligible, not_eligible). Eligible ones are sorted by priority
    (higher first). Not-eligible ones are sorted by how close the student is.
    """
    scholarships = scholarships or load_knowledge_base()
    results = [evaluate_scholarship(s, facts) for s in scholarships]
    eligible = sorted((r for r in results if r["eligible"]),
                      key=lambda r: -r["priority"])
    not_eligible = sorted((r for r in results if not r["eligible"]),
                          key=lambda r: -r["match_percent"])
    return eligible, not_eligible
