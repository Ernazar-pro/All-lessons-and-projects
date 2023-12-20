# Inheritance

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.ball=0

    
    def login(self):
        print(f'{self.name} is logged in')

    def logout(self):
        print(f'{self.name} is logged out')\

    
class Oqiwshi(User):
    def submit_task(self):
        print(f'{self.name} submitted a task')
    
    def baha_aldi(self,baha):
        print(f'{self.name} {baha} baha aldi')
        self.ball +=baha

    def get_ball(self):
       return f'{self.name} oqiwshinin balli: {self.ball}'


class Mugallim(User):
    def check_task(self):
        print(f'{self.name} checked a task')
    
    def baha_qoydi(self, object,baha):
        print(f'{self.name} mugallim {object.name} degen oqiwshiga {baha} baha qoydi ')
        object.baha_aldi(baha)


oqiwshi1=Oqiwshi('John','john@gmail.com')
oqiwshi2=Oqiwshi('Nurlan','nurlan@gmail.com')

mugallim1=Mugallim('Bob','bob@gmail.com')
mugallim2=Mugallim('Jane','jane@gmail.com')

'''
oqiwshi1.login()
oqiwshi1.submit_task()
oqiwshi1.logout()


mugallim1.login()
mugallim1.check_task()
mugallim1.logout()
'''
mugallim1.baha_qoydi(oqiwshi1,5)
mugallim2.baha_qoydi(oqiwshi1,3)

mugallim1.baha_qoydi(oqiwshi2,10)
mugallim2.baha_qoydi(oqiwshi2,5)



print(oqiwshi1.get_ball())
print(oqiwshi2.get_ball())