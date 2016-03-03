#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys

from .statareport import Reporting
from .stataspoon import MutationsTester
from .statautils import Directory, Logger

""" Report filename """
REPORT_FILENAME = 'statam_report.html'

""" Neutral processor (original tests) """
NEUTRAL_PROCESSOR = 'fr.polytech.devops.g1.stataspoon.processors.NeutralProcessor'


def main(args):
    """
    Main function.
    :param args: command-line arguments
    """
    if args.project:
        # Go to project directory
        os.chdir(os.path.abspath(args.project))

    # Clean the report directory
    Logger.log('Pre-cleaning report directory "%s"' % args.report_directory, True)
    pre_clean(args.report_directory)

    # Create mutator tester, and execute original tests
    mutator = MutationsTester(args.tests_directory, args.report_directory, not args.keep_temp)
    mutator.process(args.original)

    # Execute mutations
    mutator.process('BadassMutations',
                    ('fr.polytech.devops.g1.stataspoon.processors.operators.binary.PlusToMinusProcessor',
                     'fr.polytech.devops.g1.stataspoon.processors.operators.binary.InfEqToSupEqProcessor'))

    # Compute reporting
    report_file = os.path.join(args.report_directory, REPORT_FILENAME)
    Logger.log('=============== Generating report ===============', True)
    Reporting(args.report_directory, args.original).report(report_file)
    Logger.log('Report accessible at: %s' % os.path.abspath(report_file))


def pre_clean(directory):
    """
    Pre-clean the project.
    :param directory: report directory
    :return:
    """
    # Clean directory
    try:
        Directory.delete(directory)
    except:
        Logger.log('[Warning] Error on cleaning report directory ("%s")' % directory)

    # Create a new one
    try:
        Directory.create(directory)
    except:
        Logger.log('[Warning] Error on creating report directory ("%s")' % directory)


def get_parser():
    """
    Initialize command-line parser with default and optional arguments.
    :return: parser
    """
    # Enable command-line parsing
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument('-p', '--project',
                        help='project main directory')

    # parser.add_argument('-m', '--mutations',
    #                    help='mutations configuration file')

    parser.add_argument('-r', '--report-directory',
                        help='report output directory (generated report)',
                        default='./target/statam-report')

    parser.add_argument('-t', '--tests-directory',
                        help='tests directory (output when tests are executed)',
                        default='./target/surefire-reports')

    parser.add_argument('-g', '--original',
                        help='original (not mutated) tests directory',
                        default='_original_')

    parser.add_argument('-k', '--keep-temp',
                        help='enable/disable temporary file cleaning',
                        default=False)
    return parser


# Main execution
if __name__ == "__main__":
    # Enable logging
    Logger.ENABLED = True
    Logger.log('=============== <3 - Welcome in Mr.Statamutation project - <3 ===============', True)

    # Start the main
    sys.exit(main(
        # Parse command-line args
        get_parser().parse_args()
    ))
