from scanner.gitshield_scanner import run_scan

from reports.json_report import generate_json_report
from reports.html_report import generate_html_report
from reports.dashboard import generate_summary


findings = run_scan("test_repo")

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