#!/usr/bin/python
import argparse
import os
import sys

from .statarender import ReportRenderer
from .stataxml import JUnitReport


def main(args):
    """
    The main.
    :param args: script args
    :return: status
    """
    # Compute reports
    base_report = JUnitReport.report(os.path.join(args.tests_directory, '.'))
    mutations_reports = [
        JUnitReport.report(os.path.join(args.tests_directory, '.')),
        JUnitReport.report(os.path.join(args.tests_directory, '.')),
        JUnitReport.report(os.path.join(args.tests_directory, '.'))
    ]

    # Render the report
    ReportRenderer(base_report, mutations_reports).render_html(args.output)


def get_parser():
    """
    Initialize command-line parser with default and optional arguments.
    :return: parser
    """
    # Enable command-line parsing
    parser = argparse.ArgumentParser()

    # Default arguments
    parser.add_argument('tests_directory',
                        help='all tests main directory')

    # Optional arguments
    parser.add_argument('-o', '--output',
                        help='HTML report output file (will be overwritten)',
                        default='./statam_report.html')

    return parser


if __name__ == "__main__":
    # Start the main
    sys.exit(main(
        # Parse command-line args
        get_parser().parse_args()
    ))
