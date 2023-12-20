from Inheritance.rectangle import Rectangle

class Romb(Rectangle):
    def __init__(self, a, b,c ,d):
        super().__init__(a, b)
        self.c=c
        self.d=d
    
    def perimeter(self):
        result=self.a+self.b+self.c+self.d
        return result
    
    def square(self):
        result=(self.a*self.c+self.b*self.d)/2
        return result