import ConfigParser
import os.path

CONFIG_NAME = 'config.ini'

class Config:
    config_file = None
    config = None

    def __init__(self):
        # create file if doesn't exist
        self.config_file = open(CONFIG_NAME, 'w+')
        self.parse()
        self.config_file.close()

    def parse(self):
        if self.config_file is None:
            # not initialized
            return # TODO: debug msg

        config_text = self.config_file.read()
        self.config = ConfigParser.RawConfigParser(allow_no_value=True)
        self.config.readfp(io.BytesIO(config_text))

    def get(self, section, var):
        return self.config.get(section, var)

    def set(self, section, var, val):
        self.config.set(section, var, val)

    def dump(self):
        self.config_file = open(CONFIG_NAME, 'w')
        self.config.write(config_file)
        self.config_file.close()
