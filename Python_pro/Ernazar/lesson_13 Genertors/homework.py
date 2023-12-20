#float_range() degen generator jaratin
# range ge uqsap islesin, biraq 3-argumenti (step) float qabillay alsin.

# sebebi range(0,2,0.5) islemeydi

# for i in float_range(0,2,0.5):
# print(i)

class Float:
    def __init__(self,start:int,count:int,step):
        self.count=count
        self.i=start
        self.step=step

    def __iter__(self):
        return self
    
    def __next__(self):
        self.i +=self.step
        if self.i < self.count:
            return self.i
        
        else:
            raise StopIteration

for i in Float(0, 20, 0.5):
    print(i)