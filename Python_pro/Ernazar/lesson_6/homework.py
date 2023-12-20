# Student class jaratin, name ham age attributlari bolsin
# Student class obiektlerine jas boyinsha salistiriw imkaniyatin qosin.


# Maselen:
#
#class Student():
# ...
#
# john = Student(name='John',age=21)
# bob = Student(name='Bob',age=32)
# alice= Student(name='Alice', age=21)


# print(john > bob) # False
# print(john < bob) # True
# print(john == alice) # True shigariwi kerek


class Student:
	def __init__ (self,name: str,age: int):
		self.name=name
		self.age=age
	def __lt__ (self,other: object):
		return self.age < other.age
	def __gt__ (self,other: object):
		return self.age > other.age
	def __eq__ (self,other: object):
		return self.age == other.age

john=Student(name='john',age=21)
bob=Student(age=32,name='bob')
alice=Student(name='alice',age=21)



print(bob<john)
print(bob>john)
print(john==alice)