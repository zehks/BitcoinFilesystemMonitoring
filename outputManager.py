import os

class OutputManager():
    
    def __init__(self, 
                outputDir: str = './',
                fileName: str = 'output.csv'):

        self.outputDir = outputDir
        self.fileName = fileName

        try:
            self.absolutePath = os.path.abspath(f'{self.outputDir}/{self.fileName}')

        except Exception as e:
            print(str(e))

        finally:
            print(f'Saving data to: {self.absolutePath}')

            if not os.path.exists(self.absolutePath):
                self.saveToFile('timestamp,bytes,directories')

    def saveToFile(self, data):

        with open(self.absolutePath, 'a', encoding='utf-8') as file:
            file.writelines(f'{data}\n')