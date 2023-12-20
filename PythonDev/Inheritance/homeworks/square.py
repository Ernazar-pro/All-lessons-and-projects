from shape2 import Shape2

class Square(Shape2):
    def __init__(self,length):
        super().__init__(length)
    
    def area(self):
        if self.length == None:
            self.length= 0

        return self.length*self.length

