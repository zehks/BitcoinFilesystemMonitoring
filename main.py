from settingsManager import SettingsManager
from monitorManager import MonitorManager
from outputManager import OutputManager

from datetime import datetime, timezone
from time import sleep

def main():

    settingsManager = SettingsManager()
    monitorManager = MonitorManager()

    outputManager = OutputManager(
        settingsManager.OUTPUT_DIR,
        settingsManager.OUTPUT_FILENAME
    )

    interval = int(settingsManager.INTERVAL)
    finish = False
    while not finish:
        
        now = int(datetime.timestamp(datetime.now(timezone.utc)))
        size = monitorManager.get_fs_size(settingsManager.BITCOIN_DIR)
        
        directories = monitorManager.directories
        monitorManager.reset_directories_listing()

        outputManager.saveToFile(f'{now},{size},"{directories}"')
        
        if interval > 0:
            sleep(interval)
        else:
            finish = True
    

if __name__ == '__main__':
    main()