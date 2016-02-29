import os

from . import JUnitXMLReader

""" Tests suites counts type """
COUNTS_TYPES = ['tests', 'failures', 'errors', 'skipped']


class JUnitReport:
    """ JUnit report object model. """

    def __init__(self, name):
        self.name = name
        self.compilation_failed = False

        self.testsuites = []
        self.counts = {'success': 0}

        # Init counts to 0
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
            count = int(testsuite[type])
            self.counts[type] += count

            self.counts['success'] -= count

        self.counts['success'] += int(testsuite['tests']) * 2  # x2 because of -= in loop

    @staticmethod
    def report(name, directory):
        """
        List all JUnit XML tests suites reports and compute a report.
        :param directory: JUnit XML reports directory
        :return: report of XML files
        """
        report = JUnitReport(name)

        # Check if compilation was not a failure
        if os.path.isfile(os.path.join(directory, '.compilation_failed')):
            report.compilation_failed = True
        else:
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
