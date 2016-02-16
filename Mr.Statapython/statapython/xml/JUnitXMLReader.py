#!/usr/bin/python
import os
import xml.etree.ElementTree as Xml
import pprint


class JUnitXMLReader:
    # def __init__(self):

    @staticmethod
    def read(xmlfile):
        # Parse XML file
        root = Xml.parse(xmlfile).getroot()

        # Initialize test suite results
        testsuite = root.attrib.copy()
        testsuite['testcases'] = []

        # Check every test case results
        for element in root.iter('testcase'):
            # Initialize test case results
            testcase = element.attrib.copy()

            # Get errors
            errors = element.findall('error')

            # Failure
            if len(element.findall('failure')) > 0:
                testcase['status'] = 'failure'
            # Error
            elif len(errors) > 0:
                testcase['status'] = 'error'
                testcase['message'] = errors[0].attrib['message']
            # Success
            else:
                testcase['status'] = 'success'

            # Add the test case to the test suite
            testsuite['testcases'].append(testcase)

        # Return results
        return testsuite


if __name__ == "__main__":
    os.chdir('D:\\Google Drive\\Polytech\\_SI3\\_Semestre2\\OGL\\IslandExplorer\\target\\surefire-reports')
    pprint.pprint(
        JUnitXMLReader.read(
            'TEST-fr.unice.polytech.ogl.islcb.model.results.extras.TransformExtrasTest.xml'
        )
    )
