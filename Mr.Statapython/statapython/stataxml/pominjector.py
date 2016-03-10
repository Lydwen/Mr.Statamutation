import xml.etree.ElementTree as Xml

""" Maven XML namespace """
NS = {'mvn': 'http://maven.apache.org/POM/4.0.0'}


class PomInjector:
    """ pom.xml injector """

    def __init__(self, pom):
        """
        Load the specified pom.xml.
        :param pom: pom to load
        """
        Xml.register_namespace('', 'http://maven.apache.org/POM/4.0.0')
        self.pom = Xml.parse(pom)

    def inject_processors(self, processors):
        """
        Inject processors in the current loaded pom.
        :param processors: processors to inject
        """
        # Select <processors> node
        xml_processors = self.select_processors_element(
            self.select_plugin_element()
        )

        # Append processors
        for processor in processors:
            xml_processor = Xml.SubElement(xml_processors, 'processor')
            xml_processor.text = processor

    def inject_selectors(self, selectors):
        """
        Inject selectors in the current loaded pom.
        :param selectors: selectors to inject
        """
        # Select <configuration> node
        config = self.select_plugin_element().find('./configuration')

        # Append selectors
        for selector in selectors:
            xml_selector = Xml.SubElement(config, 'selector', {'name': selector['@name']})
            xml_parameters = Xml.SubElement(xml_selector, 'parameters')

            # Append selector parameters
            for key, value in selector.get('parameters', {}).items():
                xml_parameter = Xml.SubElement(xml_parameters, key)
                xml_parameter.text = value

    def select_plugin_element(self):
        """
        Select the spoon-maven-plugin configuration.
        :return plugin configuration
        """
        plugins = self.pom.findall('./mvn:build/mvn:plugins/mvn:plugin', NS)

        # Select the spoon-maven-plugin
        for plugin in plugins:
            # Check groupId and artifactId
            if plugin.find('./mvn:groupId', NS).text == 'fr.inria.gforge.spoon' \
                    and plugin.find('./mvn:artifactId', NS).text == 'spoon-maven-plugin':
                return plugin

    def select_processors_element(self, plugin):
        """
        Select configuration of the plugin element.
        :param plugin: plugin element
        :return: processors configuration
        """
        if plugin is None: return None

        # Get or create <configuration> node
        config = plugin.find('./mvn:configuration', NS)
        if config is None: config = Xml.SubElement(plugin, 'configuration')

        # Get or create <processors> node
        processors = config.find('./mvn:processors', NS)
        if processors is None: processors = Xml.SubElement(config, 'processors')

        return processors

    def save(self, custom_pom):
        """
        Save the current XML to specified file.
        :param custom_pom: file to save
        """
        self.pom.write(
            custom_pom,
            xml_declaration=True,
            encoding='UTF-8',
        )
