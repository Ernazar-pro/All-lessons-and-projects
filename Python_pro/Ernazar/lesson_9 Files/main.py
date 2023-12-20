class Users:
 def __init__(self, name, age, last_name) -> None:
    self.name = name 
    self.last_name = last_name 
    self = age = age 

@property
def fullname(self):
    return f'My name is {self.name} {self.last_name}, and {self.age} y.o'

def hello(self, user):
    return f'hello {user.name}, my name is {self.name}'

firstUser = Users('John','Cavil',29)
secontUser = Users('Steve','Jobs', 44) 
print(firstUser.hello(secontUser)
