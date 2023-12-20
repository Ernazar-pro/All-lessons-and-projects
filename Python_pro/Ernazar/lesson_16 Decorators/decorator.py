import time

def timer(func):
    def inner():
        started = time.time()
        func()
        finished= time.time()
        print(f'{finished-started} seconds spent')
    return inner

@timer
def do1():
    time.sleep(3)
    print('do1 is done')

@timer
def do2():
    time.sleep(2)
    print('do2 is done')

do1()
do2()
