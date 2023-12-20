# Jana Teacher classin jaratin ham ol sabaq dawaminda jaratilgan User classinan inheritance alsin
# Jana Mentor classin jaratin. Ol User classtan emes Teacher classtan inheritance alsin
# Teacher classina subclass bolgan jana Assistant classinda jaratin.

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email

class Teacher(User): 
    pass

class Mentor(Teacher):
    pass

class Assistant(Teacher):
    pass

Teacher1=Assistant('Ernazar','ernazar4507@gmail.com')
print(Teacher1.name)