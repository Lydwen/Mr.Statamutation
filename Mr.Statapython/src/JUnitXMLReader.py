#!/usr/bin/python
import os
import xml.etree.ElementTree as XML


class JUnitXMLReader:
    # def __init__(self):

    @staticmethod
    def read(xmlFile):
        root = XML.parse(xmlFile).getroot()

        print(root.attrib)

        for element in root.iter('testcase'):
            print('\t',)
            print(element.attrib)
            print(len(element.findall('failure')))


if __name__ == "__main__":
    os.chdir('D:\\Google Drive\\Polytech\\_SI3\\_Semestre2\\OGL\\IslandExplorer\\target\\surefire-reports')
    JUnitXMLReader.read(
        'TEST-fr.unice.polytech.ogl.islcb.model.results.extras.TransformExtrasTest.xml'
    )
