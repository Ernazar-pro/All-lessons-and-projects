class FileOpener:
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode
        self.opened_file= None

    def __enter__(self):
        print('Entered')
        file=open(self.filename,self.mode)
        self.opened_file=file
        return file
    def __exit__(self,exc_type,exc_value,exc_tb):
        print('Exited')
        self.opened_file.close()

with FileOpener('file2.py','w') as file:
    file.write('class User:')