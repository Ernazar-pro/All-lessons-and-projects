
class Soda:
    def __init__(self,additive):
        self.additive = additive
    def show_my_drink(self):
        if self.additive is not None:
            print('Газировка и добавка')
        else:
            print('Обычная вода')

soda = Soda('Kola')

print(soda.show_my_drink())


class TriangleChecker:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    
    def is_triangle(self):
        if self.a > 0 and self.b > 0 and self.c > 0:
            print('Ура, можно построить треугольник!')
        elif self.a < 0 and self.b < 0 and self.c < 0:
            print('С отрицательными числами ничего не выйдет!')
        elif self.a == str and self.b == str and self.c == str:
            print('Нужно вводить только числа!')
        elif (self.a + self.b) < self.c:
            print('Жаль, но из этого треугольник не сделать.')


triangle = TriangleChecker(7,8,9)

print(triangle.is_triangle())

