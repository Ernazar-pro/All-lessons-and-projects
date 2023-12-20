
def wrapper(char):
    def wrap(func):
        def inner():
            print(char * 12)
            func()
            print(char * 12)
        return inner
    return wrap

@wrapper('-')
@wrapper('%')
def hello():
    print('Hello world')

hello()