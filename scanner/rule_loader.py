import json


def load_rules(rule_file="rules/patterns.json"):
    """
    Load detection rules from JSON file.
    """

    with open(rule_file, "r") as file:
        rules = json.load(file)

    return rules