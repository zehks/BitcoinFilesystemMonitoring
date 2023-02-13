import os

from logManager import LogManager

class OutputManager():
    
    def __init__(self,
                logManager: LogManager,
                outputDir: str,
                fileName: str):

        self.outputDir = outputDir
        self.fileName = fileName
        self.logManager = logManager

        try:
            self.absolutePath = os.path.abspath(f'{self.outputDir}/{self.fileName}')

        except Exception as e:
            raise e

        finally:
            self.logManager.setDebug(f'Saving data to: {self.absolutePath}')

            if not os.path.exists(self.absolutePath):
                os.makedirs(os.path.dirname(self.absolutePath), exist_ok=True)
                self.saveToFile('timestamp,bytes,directories')

    def saveToFile(self, data):

        with open(self.absolutePath, 'a', encoding='utf-8') as file:
            file.writelines(f'{data}\n')
            self.logManager.setDebug(f'New output entry saved successfully')