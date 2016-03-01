import logging
import os

from .statautils import Directory, Logger

""" Logger """
logger = logging.getLogger()


class MutationsTester:
    """ Mutations tests launcher. """

    def __init__(self, tests_directory, report_directory):
        self.tests_directory = tests_directory
        self.report_directory = report_directory

    def clean(self):
        """
        Delete tests directory.
        """
        try:
            Directory.delete(self.tests_directory)
        except:
            Logger.log('[Warning] Error on cleaning tests directory ("%s")' % self.tests_directory)

    def process(self, processor, output_dir=None):
        """
        Execute mutation and tests.
        :param processor: processor to apply
        :param output_dir: output directory
        """
        self.clean()
        Logger.log('========================== Mutation with processor %s ==========================' % processor, True)

        # Prepare command to execute
        command = 'mvn package -Dstataprocessor="' + processor + '"'
        Logger.log('Executing command: %s' % command, False, True)

        # Post-process results
        if not (
                self.postprocess(
                    # Execute mutations and tests
                    os.system(command),
                    # Final output directory
                    os.path.join(self.report_directory, (output_dir if output_dir else processor))
                )):
            Logger.log('Compilation failed for processor: %s' % processor, True)

    def postprocess(self, status, output_dir):
        """
        Post-process.
        :param status: tests status
        :param output_dir: output directory
        :return True if compilation succeeded
        """
        try:
            # Copy results to output report directory
            Logger.log('Copying files from "%s" to "%s"...' % (self.tests_directory, output_dir), True)
            Directory.copy(self.tests_directory, output_dir)
            return True
        # Compilation failed
        except FileNotFoundError:
            # Compilation failed
            if status > 0:
                # Create an empty file to indicate the compilation failed
                Directory.touch(os.path.join(output_dir, '.compilation_failed'))
