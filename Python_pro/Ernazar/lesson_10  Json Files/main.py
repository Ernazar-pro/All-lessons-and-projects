import json

dict={
    'name':'John',
    'surname':'Smith',
    'age':23,
    'tiri': True
}


with open('baza/data.json','w') as w_file:
    json.dump(dict, w_file) # dict to json

with open('baza/data.json','r') as r_file:
    data = json.load(r_file) # json to dict



print(data)