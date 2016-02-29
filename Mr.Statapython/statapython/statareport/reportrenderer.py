from jinja2 import Environment, PackageLoader

""" Report title """
REPORT_TITLE = 'DevOps :: Mr.Statamutation :: Report'


class ReportRenderer:
    """ Report renderer. """

    def __init__(self, base_report, mutations_reports):
        self.base_report = base_report
        self.mutations_reports = mutations_reports

    def render_html(self, filepath):
        """
        Render the report as HTML.
        :param filepath: path to the HTML file output
        """
        # Get the report template
        env = Environment(loader=PackageLoader('statapython', 'templates'))
        report_template = env.get_template('report.html')

        # Render the report
        report_rendered = report_template.render(
            title=REPORT_TITLE,
            base_report=self.base_report,
            mutations_reports=self.mutations_reports
        )

        # Write the report to the file
        with open(filepath, 'w') as file:
            file.write(report_rendered)
