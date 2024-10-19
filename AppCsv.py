import os
class Csv:
    def __init__(self,file):
        if self.is_csv(file):
            self._file = file
        else:
            raise Exception

    def is_csv(self,file):
        _ , file_extension = os.path.splitext(file)
        return file_extension.lower() == '.csv'
    
    @property
    def file(self):
        return self._file
        
        

