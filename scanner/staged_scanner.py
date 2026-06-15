from scanner.rule_loader import load_rules
from scanner.file_scanner import scan_file


def scan_staged_files(files):

    rules = load_rules()

    all_findings = []

    for file in files:

        findings = scan_file(
            file,
            rules
        )

        all_findings.extend(
            findings
        )

    return all_findings