class Cat:
    def __init__(self, type,breed):
        self.type = type
        self.__breed = breed

    def friendly(self):
        return f'{self.type} - Мяу-Мяу'
    
    @property
    def move(self):
        return f'{len(self.type)}'
    

class Dog:
    def __init__(self,type) -> None:
        self.type=type
    
    def friendly(self):
        return f'{self.type} - Гав-гав'
    

cat =Cat('cat','arabian')
print(cat.move)

def main(*args):
    pass

@main
def updated_main(name):
    return f'Hi {name}'
print(updated_main)
