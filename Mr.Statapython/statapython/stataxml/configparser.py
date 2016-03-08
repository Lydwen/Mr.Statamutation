import xmltodict

""" Configuration root name """
CONFIG_ROOT = 'statam'


class ConfigParser:
    """ configuration parser """

    @staticmethod
    def parse(config_file):
        """
        Load the specified configuration.
        :param config_file: config file to load
        """
        with open(config_file, 'rb') as file:
            # Parse the configuration
            config = xmltodict.parse(file)

            # Return the root
            return config[CONFIG_ROOT]
