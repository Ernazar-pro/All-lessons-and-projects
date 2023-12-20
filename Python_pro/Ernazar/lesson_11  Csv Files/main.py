# CSV files
import csv
from pprint import pprint

data=[]

with open('C:\\Python_pro\Ernazar\\lesson_11  Csv Files\\users.csv') as file:
    for value in csv.DictReader(file):
        data.append(value)

for v in data:
    print(f"{v['name']} din jasi {v['age']} de")