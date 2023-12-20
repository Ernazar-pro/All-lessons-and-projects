from shape import Shape
import math
class Circle(Shape):
    def __init__(self, x,y,radius):
        super().__init__(x, y)
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def square(self):
        return math.pi * pow(self.radius,2)
    
    