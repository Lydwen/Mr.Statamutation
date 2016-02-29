#!/usr/bin/python
import os

from .reportrenderer import ReportRenderer
from ..stataxml import JUnitReport


class Reporting:
    """ Mutations testing report. """

    def __init__(self, tests_directory, original_directory):
        self.tests_directory = tests_directory
        self.original_directory = original_directory

    def report(self, output):
        """
        The main.
        :param output: output file
        :return: status
        """
        original_report = None
        mutations_reports = []

        # Compute reports
        for dir_name in os.listdir(self.tests_directory):
            directory = os.path.join(self.tests_directory, dir_name)

            # Check if is a directory
            if not (os.path.isdir(directory)):
                continue

            # Compute the report
            report = JUnitReport.report(dir_name, directory)

            # Original report
            if dir_name == self.original_directory:
                original_report = report
            # Mutant report
            else:
                mutations_reports.append(report)

        # Render the report
        ReportRenderer(original_report, mutations_reports).render_html(output)
