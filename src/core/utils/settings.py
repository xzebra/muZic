import configparser
import os.path
import io

CONFIG_NAME = 'config.ini'

class Config(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self)
        # create file if doesn't exist
        if not os.path.isfile(CONFIG_NAME):
            config_file = open(CONFIG_NAME, 'w+')
            config_file.close()
        self.parse()   

    def parse(self):
        self.read(CONFIG_NAME)

    def dump(self):
        with open(CONFIG_NAME, 'w') as config_file: 
            self.write(config_file)
