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

from scanner.gitshield_scanner import run_scan


def check_commit():

    findings = run_scan(".")

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