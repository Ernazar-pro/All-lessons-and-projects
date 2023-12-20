# Aldingi sabaq jaratilgan Student klassin ozgertirin
# student klasstan jaratilgan obiektti print qilganda studenttin ati shigarilsin 
# Misal:
#student=Student(name='Aziz')
#print(student)

class Student ():
    def __init__(self,name) : 
        self.name=name

    def __str__(self):
        return self.name

    
student1 = Student('Ernazar')

print(student1)