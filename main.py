from scanner.rule_loader import load_rules
from scanner.repository_scanner import scan_repository

from reports.json_report import (
    generate_json_report
)

from reports.dashboard import (
    generate_summary
)

from reports.html_report import (
    generate_html_report
)

rules = load_rules()

findings = scan_repository(
    "test_repo",
    rules
)

generate_json_report(findings)

summary = generate_summary(findings)
generate_html_report(
    findings,
    summary
)

print("\n===== GITSHIELD SUMMARY =====\n")

for severity, count in summary.items():
    print(f"{severity}: {count}")

print(f"\nTotal Findings: {len(findings)}")

print("\nFindings:\n")

for finding in findings:
    print(finding)