from shape import Shape

class Triangle(Shape):
    def __init__(self,x,y,z):
        super().__init__(x, y)
        self.z=z
    
    def perimeter(self):
        return self.x + self.y + self.z
    
    def square(self):
        return (self.z+self.y)/2
    
