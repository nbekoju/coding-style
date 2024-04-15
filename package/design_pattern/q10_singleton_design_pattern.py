# [Singleton Design Pattern] Implement a configuration manager using the Singleton Design Pattern. The configuration manager should read configuration settings from a file and provide access to these settings throughout the application. Demonstrate how the Singleton Design Pattern ensures that there is only one instance of the configuration manager, preventing unnecessary multiple reads of the configuration file.


import json


class ConfigurationManager(object):
    def __init__(self, config_file) -> None:
        self.config_file = config_file
        self.configurations = self.load_config()

    def __new__(self, config_file):
        """
        create new instance if there are no other instance, else return the current instance
        """
        if not hasattr(self, "instance"):
            self.instance = super(ConfigurationManager, self).__new__(self)
        return self.instance

    def load_config(self):
        with open(self.config_file, "r") as file:
            return json.load(file)

    def get_config(self):
        return self.configurations


config_file = "config.json"
configuration_manager_1 = ConfigurationManager(config_file)
configuration_manager_2 = ConfigurationManager(config_file)
print(configuration_manager_1 is configuration_manager_2)

config = configuration_manager_1.get_config()
print(type(config))
print(config)
