class Vector():
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    @property
    def mag(self):        # magnitudasin esaplaydi
        c=(self.x**2+self.y**2)**0.5
        return c
    def __eq__(self, other: object) -> bool:
        result=self.x == other.x and self.y == other.y
        return result
    def __add__(self,other:object):
        x=self.x + other.x
        y=self.y + other.y
        return Vector(x,y)
    def __str__(self) -> str: # class  haqqinda magliwmat
        return f'Vector<- {self.x},{self.y}->'
 
    def __sub__(self,other:object):
        x=self.x - other.x
        y=self.y - other.y
        return Vector(x,y)
    def __lt__(self,other: object):
        return self.mag < other.mag

    def __gt__(self,other: object):
        return self.mag > other.mag
v1=Vector(3,4)
v2=Vector(3,5)

#print(v1)
#print(v1.mag)
#print(v1 == v2)

v3=v1+v2
print(v3)
v4=v1-v2
print(v4)
print(v1 < v2)
print(v1 > v2)
