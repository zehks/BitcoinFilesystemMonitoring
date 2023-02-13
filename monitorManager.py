import os

class MonitorManager():

    def __init__(self):
        self.directories = []
        
    
    def get_fs_size(self, path: str) -> int:
        total = 0

        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    self.directories.append(entry.path)
                    total += self.get_fs_size(entry.path)

        return total

    def reset_directories_listing(self):
        self.directories = [] 
