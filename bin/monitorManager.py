import os

from logManager import LogManager

class MonitorManager():

    def __init__(self, logManager: LogManager, relpath: str):
        self.logManager = logManager
        self.directories = []
        self.relpath = relpath
        
    
    def get_fs_size(self, path: str = False) -> int:
        total = 0

        if path is False:
            path = self.relpath
            self.logManager.setDebug('Surfing the root filesystem')

        else:
            self.logManager.setDebug(f'Surfing {path} subdirectory.')
        
        with os.scandir(path) as it:
            for entry in it:                
                if entry.is_file():
                    self.logManager.setDebug(f'{entry.name} is a file.')
                    total += entry.stat().st_size
                    
                elif entry.is_dir():
                    self.logManager.setDebug(f'{entry} is a directory.')
                    self.directories.append(os.path.relpath(entry.path, self.relpath))
                    total += self.get_fs_size(entry.path)

        return total

    def reset_directories_listing(self):
        self.directories = []
        self.logManager.setDebug('Directories reset.')
