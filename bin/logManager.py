import os
import logging
from logging.handlers import RotatingFileHandler

class LogManager():

    def __init__(self, log_dir: str, log_level: str, log_name: str, logrotate_files: int):
        
        abs_path = os.path.abspath(f'{log_dir}/{log_name}')
        
        self.logger = logging.getLogger('monitor')
        self.logger.setLevel(self._get_level(log_level))

        if not os.path.exists(os.path.abspath(log_dir)):
            os.makedirs(os.path.dirname(abs_path), exist_ok=True)

        try:
            handler = RotatingFileHandler(
                filename = abs_path,
                maxBytes = 5242880,
                backupCount = int(logrotate_files),
                encoding = 'utf-8',
                mode = 'a'
            )
        except Exception as e:
            raise e

        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        self.logger.addHandler(handler)
        
        self.setInfo('Logger initialized successfully.')
    
    def setInfo(self, msg: str):
        self.logger.info(msg)

    def setWarn(self, msg: str):
        self.logger.warn(msg)

    def setError(self, msg: str):
        self.logger.error(msg)
    
    def setDebug(self, msg: str):
        self.logger.debug(msg)
    
    def _get_level(self, log_level: str):
        
        if log_level == 'DEBUG':
            return logging.DEBUG
        elif log_level == 'INFO':
            return logging.INFO
        elif log_level == 'WARN':
            return logging.WARN
        else:
            return logging.ERROR