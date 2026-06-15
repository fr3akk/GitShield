import re


def detect_secrets(content, rules):
    findings = []

    for rule_name, rule_data in rules.items():

        pattern = rule_data["pattern"]
        severity = rule_data["severity"]

        matches = re.finditer(pattern, content)

        for match in matches:
            findings.append(
                {
                    "type": rule_name,
                    "severity": severity,
                    "match": match.group()
                }
            )

    return findings
