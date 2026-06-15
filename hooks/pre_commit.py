import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from scanner.git_helper import get_staged_files
from scanner.staged_scanner import scan_staged_files


def check_commit():

    staged_files = get_staged_files()

    findings = scan_staged_files(staged_files)

    if findings:

        print("\n[!] GITSHIELD BLOCKED COMMIT\n")

        print(
            f"Detected {len(findings)} potential secrets:\n"
        )

        for finding in findings:

            print(
                f"[{finding['severity']}] "
                f"{finding['type']} "
                f"-> {finding['file']}"
            )

        sys.exit(1)

    print("\n[+] GitShield Scan Passed")

    sys.exit(0)


if __name__ == "__main__":
    check_commit()