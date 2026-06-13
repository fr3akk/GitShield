import os

from scanner.file_scanner import scan_file


def scan_repository(repo_path, rules):

    all_findings = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            file_path = os.path.join(root, file)

            findings = scan_file(file_path, rules)

            all_findings.extend(findings)

    return all_findings