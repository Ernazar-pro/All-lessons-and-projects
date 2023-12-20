# user.csv fayldin ishindegi har bir user ushin bolek bolek  
#JSON fayllardi ozgertetugin programma jaratin

import csv
import json
from pprint import pprint

data=[]

with open('C:\\Python_pro\\Ernazar\\lesson_11  Csv Files\\users.csv') as file:
    for value in csv.DictReader(file):
        data.append(value)



for i in range(len(data)):
    with open(f'C:\\Python_pro\\Ernazar\\lesson_11  Csv Files\\users\\user{i+1}.json','w') as file:
        json.dump(data[i],file)

