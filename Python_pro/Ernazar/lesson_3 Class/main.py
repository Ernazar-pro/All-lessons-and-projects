'''
user={
'name': 'Begis'
'surname':'Embergenov'
'fullname':'Embergenov Begis'
'age':15
}

print(user['fullname])
'''


class User():
    def __init__(self,name,surname,age) :
        self.name=name
        self.surname=surname
        self.age=age
        self.kim='oqiwshi'

    def fullname(self):
        return f'{self.name} {self.surname}'
    
    def tanistir(self):
        return f'Men {self.fullname()},{self.age} jastaman'

    def salemles(self,user):
        return f'Salem {user.name}, men {self.name}'


ernazar = User('Ernazar','Jumaniyazov', 12)
begis = User('Begis','Embergenov', 15)

print(begis.salemles(ernazar))
print(ernazar.salemles(begis))