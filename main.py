from settingsManager import SettingsManager
from monitorManager import MonitorManager

def main():

    settingsManager = SettingsManager()

    monitorManager = MonitorManager()

    size = monitorManager.get_fs_size(settingsManager.BITCOIN_DIR)
    
    print(f'{size} bytes')

if __name__ == '__main__':
    main()