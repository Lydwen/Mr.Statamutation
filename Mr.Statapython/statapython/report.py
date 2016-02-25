#!/usr/bin/python
import argparse
import os
import sys

from jinja2 import Environment, PackageLoader

from .stataxml import JUnitReport

args = []  # Script arguments


def main():
    # Get report infos
    report = JUnitReport.report(os.path.join(args.mutants_directory, args.testsdir))

    # Display infos
    print(report.testsuites)
    print(report.counts)


def render(base_report, mutations_reports):
    # Get the report template
    env = Environment(loader=PackageLoader('statapython', 'templates'))
    report_template = env.get_template('report.html')

    # Render the report
    report_rendered = report_template.render(
        title='DevOps :: Mr.Statamutation :: Report',
        prog_report=base_report,
        mutations_reports=mutations_reports
    )

    # Write the report to the file
    with open('statam_report.html', 'w') as file:
        file.write(report_rendered)


def get_parser():
    # Enable command-line parsing
    parser = argparse.ArgumentParser()

    # Needed arguments
    parser.add_argument("mutants_directory",
                        help="all mutants main directory")

    # Optional arguments
    parser.add_argument("--testsdir",
                        help="tests results sub-directory",
                        default="target/surefire-reports")
    parser.add_argument('-o', '--output',
                        help="output HTML report file (will be overwritten)",
                        default='statam_report.html')

    return parser


if __name__ == "__main__":
    # Parse command-line args
    args = get_parser().parse_args()

    # Start the main
    sys.exit(main())
