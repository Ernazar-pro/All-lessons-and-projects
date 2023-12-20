# Decorators 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def tms(a,b):
    return a*b

def calc(func,a,b):
    return func(a,b)

print(calc(sub,3,4))