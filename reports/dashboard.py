from collections import Counter


def generate_summary(findings):

    severities = [
        finding["severity"]
        for finding in findings
    ]

    return Counter(severities)