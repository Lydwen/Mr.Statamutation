import logging
import os

from ..statautils import Directory, Logger
from ..stataxml import PomInjector

""" Original pom.xml filename """
POM_FILENAME = 'pom.xml'

""" Custom pom.xml filename """
CUSTOM_POM_FILENAME = 'poir.xml'

""" Logger """
logger = logging.getLogger()


class MutationsTester:
    """ Mutations tests launcher. """

    def __init__(self, tests_directory, report_directory, postprocess_clean):
        self.tests_directory = tests_directory
        self.report_directory = report_directory
        self.postprocess_clean = postprocess_clean

    def clean(self):
        """
        Delete tests directory.
        """
        try:
            Directory.delete(self.tests_directory)
        except:
            Logger.log('[Warning] Error on cleaning tests directory ("%s")' % self.tests_directory)

    def inject_processors(self, processors, filename):
        """
        Inject processors in a custom pom.xml file.
        :param processors: processors to inject
        :param filename: custom pom.xml filename
        :return: path to the custom pom.xml
        """
        # Injector processors
        injector = PomInjector(POM_FILENAME)
        injector.inject_processors(processors)

        # Save to the new file
        injector.save(filename)
        return filename

    def process(self, name, processors=(), selectors=()):
        """
        Execute mutation and tests.
        :param name: output directory
        :param processors: processor to apply
        :param selectors: selectors to apply
        """
        self.clean()
        Logger.log('========================== Mutation "%s" ==========================' % name,
                   True)

        # Inject processors
        Logger.log('Injecting processors in "%s": %s' % (CUSTOM_POM_FILENAME, processors))
        pom_file = self.inject_processors(processors, CUSTOM_POM_FILENAME)

        # Prepare command to execute
        command = 'mvn package -f "%s"' % pom_file
        Logger.log('Executing command: %s' % command, False, True)

        # Post-process results
        if not (
                self.postprocess(
                    # Execute mutations and tests
                    os.system(command),
                    # Final output directory
                    os.path.join(self.report_directory, name),
                    pom_file
                )):
            Logger.log('Compilation failed for processors: %s' % (processors,), True)

    def postprocess(self, status, output_dir, pom_file):
        """
        Post-process.
        :param status: tests status
        :param output_dir: output directory
        :param pom_file: custom pom file
        :return True if compilation succeeded
        """
        try:
            # Copy results to output report directory
            Logger.log('Copying files from "%s" to "%s"...' % (self.tests_directory, output_dir))
            Directory.copy(self.tests_directory, output_dir)
            return True
        # Compilation failed
        except FileNotFoundError:
            # Compilation failed
            if status > 0:
                # Create an empty file to indicate the compilation failed
                Directory.touch(os.path.join(output_dir, '.compilation_failed'))
        finally:
            # Remove the temporary custom pom file
            if self.postprocess_clean:
                Logger.log('Removing temporary "%s" file...' % pom_file, True)
                os.remove(pom_file)
