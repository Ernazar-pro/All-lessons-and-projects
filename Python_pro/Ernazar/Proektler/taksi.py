class Taksi:
   def __init__(self,marka) :
       self.marka=marka
       self.jolawshilar = []
   
   def get_jolawshilar(self):
        return[jolawshi.get_name() for jolawshi in self.jolawshilar]

   def jolawshi_aliw(self, jolawshi: object):
    self.jolawshilar.append(jolawshi)

class Adam:
    def __init__(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
    def taksige_miniw(self,taksi: object):
        print(f'{self.name} {taksi.marka}  taksige mindi')
        taksi.jolawshi_aliw(self)

    

adam1=Adam('Begis')
adam2=Adam('Ernazar')
adam3=Adam('Nurlan')

taksi1=Taksi('cobalt')


adam1.taksige_miniw(taksi1)
adam2.taksige_miniw(taksi1)
adam3.taksige_miniw(taksi1)

print(taksi1.get_jolawshilar())