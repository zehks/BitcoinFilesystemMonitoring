from configparser import ConfigParser

DEFAULT = 'DEFAULT'

class SettingsManager():
    
    def __init__(self):
        
        configparser = ConfigParser()

        configparser.read('settings.conf')

        self.BITCOIN_DIR = configparser.get(DEFAULT, 'BitcoinDir')
        
        self.INTERVAL = configparser.get(DEFAULT, 'CheckInterval')

        self.OUTPUT_DIR = configparser.get(DEFAULT, 'OutputDir')
        self.OUTPUT_FILENAME = configparser.get(DEFAULT, 'OutputFilename')
