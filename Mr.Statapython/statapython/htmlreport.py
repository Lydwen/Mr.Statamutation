#!/usr/bin/python
import sys
import os
import argparse

from stataxml import JUnitReport


def main(args):
    # Get report infos
    report = JUnitReport.report(os.path.join(args.mutants_directory, args.testsdir))

    # Display infos
    print(report.testsuites)
    print(report.counts)


if __name__ == "__main__":
    # Enable command-line parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("mutants_directory", help="all mutants main directory")
    parser.add_argument("--testsdir", help="tests results sub-directory", default="target/surefire-reports")

    # Start the main
    sys.exit(main(parser.parse_args()))
