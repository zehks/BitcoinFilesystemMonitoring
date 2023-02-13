from configparser import ConfigParser

DEFAULT = 'DEFAULT'
LOGGER = 'LOGGER'

class SettingsManager():
    
    def __init__(self):
        
        try:

            configparser = ConfigParser()

            configparser.read('settings.conf')

            self.BITCOIN_DIR = configparser.get(DEFAULT, 'BitcoinDir')
            
            self.INTERVAL = configparser.get(DEFAULT, 'CheckInterval')

            self.OUTPUT_DIR = configparser.get(DEFAULT, 'OutputDir')
            self.OUTPUT_FILENAME = configparser.get(DEFAULT, 'OutputFilename')

            self.LOG_DIR = configparser.get(LOGGER, 'LogDir')
            self.LOG_LEVEL = configparser.get(LOGGER, 'LogLevel')
            self.LOG_FILENAME = configparser.get(LOGGER, 'LogFilename')
            self.LOG_ROTATE_MAX_FILES = configparser.get(LOGGER, 'LogRotateMaxFiles')
        
        except Exception as e:
            raise e