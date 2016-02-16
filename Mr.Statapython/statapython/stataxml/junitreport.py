import os

from . import JUnitXMLReader

""" Tests suites counts type """
COUNTS_TYPES = ['tests', 'failures', 'errors', 'skipped']


class JUnitReport:
    def __init__(self):
        self.testsuites = []

        # Init counts to 0
        self.counts = {}
        for type in COUNTS_TYPES:
            self.counts[type] = 0

    def add_testsuite(self, testsuite):
        """
        Add a tests suite to this report.
        :param testsuite: tests suite to add
        """
        self.testsuites.append(testsuite)

        # Add counts
        for type in COUNTS_TYPES:
            self.counts[type] += int(testsuite[type])

    @staticmethod
    def report(directory):
        """
        List all JUnit XML tests suites reports and compute a report.
        :param directory: JUnit XML reports directory
        :return: report of XML files
        """
        report = JUnitReport()

        # Get all files in the specified direction
        for file in os.listdir(directory):
            # Check if the file is a test XML report file
            if file.startswith('TEST-') and file.endswith('.xml'):
                # Add the test suite results
                report.add_testsuite(
                    # Parse the test suite
                    JUnitXMLReader.read_testsuite(os.path.join(directory, file))
                )

        return report
