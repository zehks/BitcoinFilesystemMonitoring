from logManager import LogManager
from settingsManager import SettingsManager
from monitorManager import MonitorManager
from outputManager import OutputManager

from datetime import datetime, timezone
from time import sleep

def main():

    try:
        

        settingsManager = SettingsManager()

        logManager = LogManager(
            log_dir = settingsManager.LOG_DIR,
            log_name = settingsManager.LOG_FILENAME,
            log_level = settingsManager.LOG_LEVEL,
            logrotate_files = settingsManager.LOG_ROTATE_MAX_FILES
        )

        monitorManager = MonitorManager(logManager, settingsManager.BITCOIN_DIR)

        outputManager = OutputManager(
            logManager,
            settingsManager.OUTPUT_DIR,
            settingsManager.OUTPUT_FILENAME
        )

        interval = int(settingsManager.INTERVAL)
        finish = False
        interval = 0.01
    except Exception as e:
        logManager.setError(str(e))
        print(str(e))
        return

    try:

        while not finish:
            logManager.setInfo(f'Starting to surf {settingsManager.BITCOIN_DIR}')

            now = int(datetime.timestamp(datetime.now(timezone.utc)))
            size = monitorManager.get_fs_size()
            
            directories = monitorManager.directories
            monitorManager.reset_directories_listing()

            outputManager.saveToFile(f'{now},{size},"{directories}"')
            
            logManager.setInfo(f'Finished, sleeping for {str(interval)} seconds.')
            if interval > 0:
                sleep(interval)
                logManager.setInfo('Wake up!')
                
            else:
                finish = True

    except Exception as e:
        logManager.setError(str(e))
        print(str(e))
        return
    

if __name__ == '__main__':
    main()