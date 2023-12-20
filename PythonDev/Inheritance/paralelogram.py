from Inheritance.rectangle import Rectangle

class Paralelogram(Rectangle):
      def __init__(self, a, b):
        super().__init__(a, b)
        
    
      def perimeter(self):
          result= 2*(self.a+self.b)
          return result
      
      def square(self):
          result= self.a*self.b
          return result
            
    