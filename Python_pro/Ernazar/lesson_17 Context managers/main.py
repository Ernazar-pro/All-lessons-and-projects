
from contextlib import contextmanager

@contextmanager
def file_opener(filename,mode):
    file = open(filename,mode)
    print('File opened')
    try:
        yield file
        print('File closed')
    finally:
        file.close()

with file_opener('main.py','w') as file:
    file.write('hello world2')
    print('File written')