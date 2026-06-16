import json
import os

from reports.masking import mask_secret


def generate_json_report(
    findings,
    output_file="output/findings.json"
):

    os.makedirs(
        "output",
        exist_ok=True
    )

    masked_findings = []

    for finding in findings:

        masked_finding = finding.copy()

        if "match" in masked_finding:

            masked_finding["match"] = (
                mask_secret(
                    masked_finding["match"]
                )
            )

        masked_findings.append(
            masked_finding
        )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as report:

        json.dump(
            masked_findings,
            report,
            indent=4
        )

    return output_file