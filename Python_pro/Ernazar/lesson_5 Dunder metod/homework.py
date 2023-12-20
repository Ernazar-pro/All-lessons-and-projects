class Magliwmat():
    def __init__(self) :
        self.dicts={}
    def qosiw(self,key,value):
            self.dicts[key]=value
    def value (self,key):
            val=self.dicts[key]
            return val
    def size (self):
           return len(self.dicts)
    def delete (self,key):
            del(self.dicts[key])
    def table (self):
            for key in self.dicts.keys():
                print(f'{key}:{self.dicts[key]}')

info1=Magliwmat()
info1.qosiw('pen','ruchka')
info1.qosiw('pencil','qalem')
info1.qosiw('dog','iyt')

print(info1.dicts)
print(info1.value('pen'))
print(info1.size())

info1.delete('dog')
print(info1.size())

info1.table()
