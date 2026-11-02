"""Command-line version (no Streamlit needed). Run: python cli.py"""
from engine import evaluate_all


def ask(prompt, options=None, cast=str):
    while True:
        raw = input(prompt + (f" {options}" if options else "") + ": ").strip()
        try:
            val = cast(raw)
            if options is None or val in options:
                return val
        except ValueError:
            pass
        print("Invalid input, try again.")


facts = {
    "category": ask("Category", ["General", "EWS", "OBC", "SC", "ST"]),
    "gender": ask("Gender", ["Male", "Female", "Other"]),
    "state": ask("Home state (type exactly, e.g. Himachal Pradesh)"),
    "income": ask("Annual family income (Rs)", cast=float),
    "cgpa": ask("CGPA", cast=float),
    "level": ask("Level", ["Undergraduate", "Postgraduate", "Diploma"]),
    "course": ask("Course", ["B.Tech / Engineering", "Science", "Commerce", "Arts", "Other"]),
    "disability": ask("Disability 40%+ (yes/no)", ["yes", "no"]) == "yes",
}

eligible, not_eligible = evaluate_all(facts)
print("\n=== ELIGIBLE ===")
for r in eligible:
    print(f"* {r['name']} - {r['benefit']}")
    for p in r["passed"]:
        print(f"    + {p}")
print("\n=== NOT ELIGIBLE ===")
for r in not_eligible:
    print(f"* {r['name']} ({r['match_percent']}% met)")
    for f in r["failed"]:
        print(f"    - Not met: {f}")
