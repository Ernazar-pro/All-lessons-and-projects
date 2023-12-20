from Inheritance.rectangle import Rectangle
from square import Square
from paralelogram import Paralelogram
from romb import Romb

shape_1=Rectangle(5,4)
print(f'P:{shape_1.perimeter()} \nS:{shape_1.square()}')

print('-------------------------------------------------')

shape_2=Square(6,None)
print(f'P:{shape_2.perimeter()} \nS:{shape_2.square()}')

print('-------------------------------------------------')

shape_3=Paralelogram(7,8)
print(f'P:{shape_3.perimeter()} \nS:{shape_3.square()}')

print('-------------------------------------------------')

shape_4=Romb(8,8,8,8)
print(f'P:{shape_4.perimeter()} \nS:{shape_4.square()}')