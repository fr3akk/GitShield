from scanner.gitshield_scanner import run_scan

findings = run_scan(
    "test_repo"
)

print(
    f"Findings: {len(findings)}"
)

for finding in findings:
    print(finding)