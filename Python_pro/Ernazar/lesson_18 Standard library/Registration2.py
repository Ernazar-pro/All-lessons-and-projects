import re

forms=[
    {'name':'Username','soraw':'Username kiritin: ','ulgi':'^[a-z0-9_-]{3,15}$'},
    {'name':'Password','soraw':'Password kiritin: ','ulgi':'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'},
    {'name':'Number','soraw':'Number kiritin: ','ulgi':'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'}]



for form in forms:
    while True:
        juwap = input(form['soraw'])
        check = re.match(form['ulgi'],juwap)
        if check == None:
            print('Qabillanbadi')
        else:
            print('Qabillandi')
            break
        