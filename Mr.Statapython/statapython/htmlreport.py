#!/usr/bin/python
import os
import pprint
import sys

from stataxml import JUnitXMLReader


def main():
    os.chdir('D:\\Google Drive\\Polytech\\_SI3\\_Semestre2\\OGL\\IslandExplorer\\target\\surefire-reports')
    pprint.pprint(
        JUnitXMLReader.read(
            'TEST-fr.unice.polytech.ogl.islcb.model.results.extras.TransformExtrasTest.xml'
        )
    )


if __name__ == "__main__":
    sys.exit(main())
