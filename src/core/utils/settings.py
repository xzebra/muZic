import configparser
import os.path
import io
from core.utils import color

CONFIG_NAME = 'config.ini'

class Config(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self)
        # create file if doesn't exist
        if not os.path.isfile(CONFIG_NAME):
            config_file = open(CONFIG_NAME, 'w+')
            config_file.close()
        self.parse()   

    def is_set(self, var, section='main'):
        attrib = self.get(section, var)
        return attrib is not None and len(attrib) != 0
    
    def require(self, var, section='main'):
        if not self.is_set(var, section):
            color.display_messages('you have to configure the {}'.format(var), error=True)
            return False
        return True

    def parse(self):
        self.read(CONFIG_NAME)

    def dump(self):
        with open(CONFIG_NAME, 'w') as config_file: 
            self.write(config_file)
