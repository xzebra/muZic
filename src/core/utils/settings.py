import configparser
import os.path
import io
from src.core.utils import color

CONFIG_NAME = 'muZic.cfg'

class Config(configparser.ConfigParser):
    # generate a path to the user folder depending on the OS
    path = os.path.expanduser('~/{}'.format(CONFIG_NAME))
    def __init__(self):
        configparser.ConfigParser.__init__(self)
        # create file if doesn't exist
        if not os.path.isfile(self.path):
            config_file = open(self.path, 'w+')
            config_file.close()
        self.parse()   

    def is_set(self, var, section='main'):
        attrib = self.get(section, var)
        return attrib is not None and len(attrib) != 0
    
    def require_one(self, var, section='main'):
        if not self.is_set(var, section):
            color.display_messages('you have to configure the {}'.format(var), error=True)
            return False
        return True

    def require(self, var_list, section='main'):
        for var in var_list:
            if not self.require_one(var):
                return False
        return True

    def __getitem__(self, key, section='main'):
        return self.get(section, key)

    def parse(self):
        self.read(self.path)

    def dump(self):
        with open(self.path, 'w') as config_file: 
            self.write(config_file)
