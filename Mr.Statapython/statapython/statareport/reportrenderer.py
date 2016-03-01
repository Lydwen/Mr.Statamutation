import os
import zipfile

import pkg_resources
from jinja2 import Environment, PackageLoader

from ..statautils import Logger

""" Reporting character encoding """
REPORT_ENCODING = 'UTF-8'

""" Report title """
REPORT_TITLE = 'DevOps :: Mr.Statamutation :: Report'

""" Report theme zip file """
REPORT_THEME = pkg_resources.resource_filename('statapython.templates', 'theme.zip')


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
        with open(filepath, 'wb') as file:
            file.write(report_rendered.encode(REPORT_ENCODING))

        # Extract the theme
        self.extract_theme(os.path.dirname(filepath))

    def extract_theme(self, directory):
        """
        Extract the theme to the report directory.
        :param directory: report directory
        """
        Logger.log('Extracting theme in the report directory...')
        # Extract the theme
        with zipfile.ZipFile(REPORT_THEME, 'r') as theme:
            theme.extractall(directory)
