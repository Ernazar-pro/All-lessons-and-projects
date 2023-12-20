from random import *

#print(randint(0,10))


m = ['Python', 'Java', 'JavaScript', 'Jango', 'C++']
#print(choice(m))

n=[1,2,3,4,5,6]
shuffle(n)
#print(n)


for i in zip(m,n):
    print(i)