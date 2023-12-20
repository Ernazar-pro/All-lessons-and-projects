

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    

rectangle=Rectangle(6,7)
print(rectangle.area())