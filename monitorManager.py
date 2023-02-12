import os

class MonitorManager():

    def __init__(self):
        self.var = 'a'
    
    def get_fs_size(self, path: str) -> int:

        total = 0
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    total += entry.stat().st_size
                elif entry.is_dir():
                    total += self.get_fs_size(entry.path)
        return total
