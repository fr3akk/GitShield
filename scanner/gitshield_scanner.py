from scanner.rule_loader import load_rules
from scanner.repository_scanner import scan_repository


def run_scan(repo_path):

    rules = load_rules()

    findings = scan_repository(
        repo_path,
        rules
    )

    return findings