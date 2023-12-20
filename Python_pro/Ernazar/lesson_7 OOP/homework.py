
# Student degen class jaratin, classtin 'name' ham 'surname' degen atributlari bolsin
#
# Classqa 'from_fullname' degen class metod qosin, toliq atti qabillasin
# ham qabillagan stringnen 'name' ham 'surname' lerdi ajiratip alip student jaratsin
#
# Maselen:
# student = Student.from_fullname('John Smith')
# print(student.name) -> 'John'
# print(student.surname) -> 'Smith
class Student():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    
    @classmethod
    def from_fullname(cls,fullname):
        name,surname=fullname.split()
        return cls(name, surname )
    
student1=Student.from_fullname('Ernazar Jumaniyazov')
print(student1.name)