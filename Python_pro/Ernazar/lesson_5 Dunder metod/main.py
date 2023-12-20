


# i18n -> internationalization
# k8n -> kubernation

# dunder -> double underscore

class Array():
    def __init__(self):
        self.elements=[]
    def qosiw(self, element):
        self.elements.append(element)
    def __izdegi__(self):
        return self.elements[-1]
    def size (self):
        return len(self.elements)
    def __len__ (self):
        return len(self.elements)
    def oshiriw(self,element):
        self.elements.remove(element)
    def __str__(self):
        return f'Elements:{ self.elements}, Size: {len(self)}'
    



ar=Array()


ar.qosiw('Ernazar')
ar.qosiw('Erlan')
ar.qosiw('Aziz')
ar.qosiw('Begis')
ar.qosiw('Alisher')

#print(ar.size())
#print( for t(dir(ar))


#for metod in dir(ar):
#   print(metod)

import turtle
t=turtle.Turtle()

for m in dir(t):
    print(m)