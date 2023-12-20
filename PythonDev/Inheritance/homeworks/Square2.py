from shape import Shape

class Square(Shape):
    def __init__(self,x,y):
        super().__init__(x, y)
    
    def perimeter(self):
        return self.x*4
    
    def square(self):
        return pow(self.x,2)


