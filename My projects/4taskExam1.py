

class Gadget:
    def __init__(self,title,quality,description,made):
        self.title = title
        self.quality = quality
        self.description = description
        self.made = made
    
    def name(self):
        return self.title
    


class Laptop():
    def __init__(self,title,quality,description,made):
        self.title = title
        self.quality = quality
        self.description = description
        self.made = made

    
    def name(self):
        return self.title



laptop=Laptop(title='Lenovo',quality='high',description='legibli',made='Slovakia')
print(laptop.name())