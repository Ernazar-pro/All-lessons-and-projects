from Inheritance.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, a, b):
        super().__init__(a, b)
    
    def perimeter(self):
        result = self.a *4
        return result
    def square(self):
        result = pow(self.a,2)
        return result
