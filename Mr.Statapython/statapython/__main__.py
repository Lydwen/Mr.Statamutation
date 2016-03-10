#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import sys
import webbrowser

from .statareport import Reporting
from .stataspoon import MutationsTester
from .statautils import Directory, Logger
from .stataxml import ConfigParser

""" Report filename """
REPORT_FILENAME = 'statam_report.html'


def main(args):
    """
    Main function.
    :param args: command-line arguments
    """
    if args.project:
        # Go to project directory
        os.chdir(os.path.abspath(args.project))

    # Check if Spoon need to be applied
    if not args.disable_spoon:
        # Clean the report directory
        Logger.log('Pre-cleaning report directory "%s"' % args.report_directory, True)
        pre_clean(args.report_directory)

        # Load the configuration
        Logger.log('Load mutations configuration "%s"' % args.mutations_config, True)
        mutations_config = ConfigParser.parse(args.mutations_config)

        # Create mutator tester, and execute original tests
        mutator = MutationsTester(args.tests_directory, args.report_directory, not args.keep_temp)
        mutator.process(args.original)

        # Get all mutations
        mutations = mutations_config['mutations']['mutation']
        if not isinstance(mutations, (list, tuple)): mutations = (mutations,)  # Bind to list

        # Execute every mutations
        for mutation in mutations:
            mutator.process(mutation['name'], mutation['processors']['processor'])

    # Check if report generation is enabled
    if not args.disable_report:
        # Compute reporting
        report_file = os.path.join(args.report_directory, REPORT_FILENAME)
        report_abspath = os.path.abspath(report_file)
        Logger.log('=============== Generating report ===============', True)
        Reporting(args.report_directory, args.original).report(report_file)
        Logger.log('Report accessible at: %s' % report_abspath)

        # Open in browser if asked to
        if args.open_browser:
            Logger.log('Opening report file in browser...')
            webbrowser.open(report_abspath)


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

    parser.add_argument('-m', '--mutations-config',
                        help='mutations configuration file',
                        default='./statamutations.xml')

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
                        action='store_true')

    parser.add_argument('-o', '--open-browser',
                        help='open the report file in the default browser after generation',
                        action='store_true')

    parser.add_argument('--disable-spoon',
                        help='disable Spoon (only the report will be computed)',
                        action='store_true')

    parser.add_argument('--disable-report',
                        help='disable report generation (only Spoon will be applied)',
                        action='store_true')
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
