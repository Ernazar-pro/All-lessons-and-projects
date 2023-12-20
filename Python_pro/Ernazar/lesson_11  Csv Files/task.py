import csv
from pprint import pprint

data=[]

with open('C:\Python_pro\Ernazar\lesson_11  Csv Files\grade.csv') as file:
    for value in csv.DictReader(file):
        data.append(value)

data_5=[]

for v in data:
    if v['grade']=='5':
        data_5.append(v['subject'])

print(data_5)