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
    original_report = None
    mutations_reports = []

    # Compute reports
    for dir_name in os.listdir(args.tests_directory):
        directory = os.path.join(args.tests_directory, dir_name)

        # Check if is a directory
        if not (os.path.isdir(directory)):
            continue

        # Compute the report
        report = JUnitReport.report(directory)

        # Original report
        if dir_name == args.original:
            original_report = report
        # Mutant report
        else:
            mutations_reports.append(report)

    # Render the report
    ReportRenderer(original_report, mutations_reports).render_html(args.output)


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
    parser.add_argument('-g', '--original',
                        help='original (not mutated) tests directory',
                        default='original')

    return parser


if __name__ == "__main__":
    # Start the main
    sys.exit(main(
        # Parse command-line args
        get_parser().parse_args()
    ))
