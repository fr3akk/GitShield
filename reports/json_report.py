import json
import os


def generate_json_report(findings,
                         output_file="output/findings.json"):

    os.makedirs("output", exist_ok=True)

    with open(output_file,
              "w",
              encoding="utf-8") as report:

        json.dump(
            findings,
            report,
            indent=4
        )

    return output_file