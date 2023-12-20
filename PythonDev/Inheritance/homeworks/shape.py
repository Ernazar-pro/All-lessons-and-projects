

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def perimeter(self):
        return 2*(self.x+self.y)
    
    def square(self):
        return self.x*self.y

