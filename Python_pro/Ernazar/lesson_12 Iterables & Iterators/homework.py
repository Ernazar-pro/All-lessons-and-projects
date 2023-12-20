# for loop arqali hesh qashan toqtamaytugin (infinite loop) programma duzin

class Counter:
    def __init__(self,start:int,count:int,step:int):
        self.count=count
        self.i=start
        self.step=step

    def __iter__(self):
        print('Inheration started')
        return self
    
    def __next__(self):
        self.step +=self.count
        if self.i < self.count:
            return self.i
        else:
            raise StopIteration

for i in Counter(1,10,2):
    print(i)
        