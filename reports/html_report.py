from jinja2 import Environment
from jinja2 import FileSystemLoader


def generate_html_report(
    findings,
    summary
):

    env = Environment(
        loader=FileSystemLoader(
            "reports"
        )
    )

    template = env.get_template(
        "report_template.html"
    )

    html = template.render(

        findings=findings,

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
        )

    )

    with open(
        "output/scan_report.html",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(html)