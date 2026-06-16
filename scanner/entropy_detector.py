import math
import re
from collections import Counter


def calculate_entropy(text):

    if not text:
        return 0

    frequency = Counter(text)

    length = len(text)

    entropy = 0

    for count in frequency.values():

        probability = count / length

        entropy -= probability * math.log2(probability)

    return entropy


def detect_high_entropy_strings(content,
                                threshold=3.8,
                                min_length=20):

    findings = []

    tokens = re.findall(
        r"[A-Za-z0-9_\-]{20,}",
        content
    )

    for token in tokens:

        entropy = calculate_entropy(token)

        if entropy >= threshold:

            findings.append(
                {
                    "type": "High Entropy String",
                    "severity": "Medium",
                    "match": token,
                    "entropy": round(entropy, 2)
                }
            )

    return findings