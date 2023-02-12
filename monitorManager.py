import os

class MonitorManager():

    def __init__(self):
        self.directories = []
        self.total = 0
    
    def get_fs_size(self, path: str) -> int:

        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    self.total += entry.stat().st_size
                elif entry.is_dir():
                    self.directories.append(entry.path)
                    self.total += self.get_fs_size(entry.path)

        return self.total

    def reset_directories_listing(self):
        self.directories = [] 
