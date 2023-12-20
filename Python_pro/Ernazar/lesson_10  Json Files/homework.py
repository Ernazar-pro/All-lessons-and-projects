# Rundi basqan gezde input arqali fayldin atin sorasin
# keyin magliwmatlardi sorasin
# magliwmatlardi kiritkennen keyin sol magliwmatlardi oz ishine algan file jaratsin 


import json
l=input('File name:')

data={}
name=input('Name: ')
data['Name']=name

surname=input('Surname:')
data['Surname']=name

age=input('Age: ')
data['Age']=age

with open(f'{l}.json','w') as file:
    json.dump(data, file)