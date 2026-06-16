from datetime import datetime

from jinja2 import Environment
from jinja2 import FileSystemLoader

from reports.masking import mask_secret


def generate_html_report(
    findings,
    summary
):

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

    env = Environment(
        loader=FileSystemLoader(
            "reports"
        )
    )

    template = env.get_template(
        "report_template.html"
    )

    html = template.render(

        findings=masked_findings,

        critical=summary.get(
            "Critical",
            0
        ),

        high=summary.get(
            "High",
            0
        ),

        medium=summary.get(
            "Medium",
            0
        ),

        total=len(findings),

        files_scanned=len(
            set(
                finding["file"]
                for finding in findings
            )
        ),

        generated_at=datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    )

    with open(
        "output/scan_report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)