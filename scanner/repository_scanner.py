import os

from scanner.file_scanner import scan_file


EXCLUDED_DIRS = {
    ".git",
    "venv",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "output",
    "examples"
}

EXCLUDED_FILES = {
    
    "requirements.txt",
    "entropy_detector.py",
    "file_scanner.py",
    "README.md"
}


def scan_repository(repo_path, rules):

    all_findings = []

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in EXCLUDED_DIRS
        ]

        for file in files:

            if file in EXCLUDED_FILES:
                print(f"Skipping: {file}")
                continue
                
            file_path = os.path.join(
                root,
                file
            )

            findings = scan_file(
                file_path,
                rules
            )

            all_findings.extend(
                findings
            )

    return all_findings