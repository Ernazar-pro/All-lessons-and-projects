# lambda arguments : expression

'''
def my_func(x):
    return x + 10
'''

'''
my_func = lambda x: x+10

print(my_func(5))
'''

'''
qosiw = lambda a,b,c : a + b + c

print(qosiw(4,5,7))
'''

def dareje(a):
    return lambda x: x**a

kv=dareje(2)
kub=dareje(4)

print(kv(4))