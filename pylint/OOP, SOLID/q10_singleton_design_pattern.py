"""
Implement a configuration manager using the Singleton Design Pattern. 
The configuration manager should read configuration settings from a file and 
provide access to these settings throughout the application. 
Demonstrate how the Singleton Design Pattern ensures that there is only one instance of 
the configuration manager, preventing unnecessary multiple reads of the configuration file.
"""

import json


class ConfigurationManager():
    """
    Configuration manager
    
    Attributes:
        config_file: name of the config_file
    """
    def __init__(self, config_file) -> None:
        self.config_file = config_file
        self.configurations = self.load_config()

    def __new__(cls):
        """
        create new instance if there are no other instance, else return the current instance
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(ConfigurationManager, cls).__new__(cls)
        return cls.instance

    def load_config(self):
        """
        load the json config from the given config_file
        """
        with open(self.config_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_config(self):
        """
        return the configurations json
        """
        return self.configurations


CONFIG_FILE = "config.json"
configuration_manager_1 = ConfigurationManager(CONFIG_FILE)
configuration_manager_2 = ConfigurationManager(CONFIG_FILE)
print(configuration_manager_1 is configuration_manager_2)

config = configuration_manager_1.get_config()
print(type(config))
print(config)
