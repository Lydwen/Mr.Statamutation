import xml.etree.ElementTree as Xml


class JUnitXMLReader:
    """ JUnit XML files reader. """

    @staticmethod
    def read_testsuite(file):
        """
        Parse the specified XML file and compute tests suite results.
        :param file: XML report to read
        :return: tests suite results
        """
        # Parse XML file
        root = Xml.parse(file).getroot()

        # Initialize test suite results
        testsuite = root.attrib.copy()
        testsuite['shortname'] = testsuite['name'].split('.')[-1]
        testsuite['testcases'] = []

        # Check every test case results
        for element in root.iter('testcase'):
            # Initialize test case results
            testcase = element.attrib.copy()
            del testcase['classname']  # Useless (already in testsuite)

            # Get errors
            errors = element.findall('error')

            # Failure
            if len(element.findall('failure')) > 0:
                testcase['status'] = 'failure'
            # Error
            elif len(errors) > 0:
                testcase['status'] = 'error'
                testcase['message'] = errors[0].attrib.get('message', None)
            # Success
            else:
                testcase['status'] = 'success'

            # Add the test case to the test suite
            testsuite['testcases'].append(testcase)

        # Return results
        return testsuite
