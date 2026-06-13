from scanner.regex_detector import detect_secrets
from scanner.entropy_detector import detect_high_entropy_strings


def scan_file(file_path, rules):

    findings = []

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read()

        regex_findings = detect_secrets(
            content,
            rules
        )

        entropy_findings = (
            detect_high_entropy_strings(
                content
            )
        )

        combined_findings = (
            regex_findings +
            entropy_findings
        )

        for finding in combined_findings:

            finding["file"] = file_path

            findings.append(finding)

    except UnicodeDecodeError:
        return []

    except Exception as error:
            print(
            f"Error scanning {file_path}: {error}"
        )

    return []