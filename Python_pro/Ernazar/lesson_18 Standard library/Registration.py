import re

while True:
        username=input('Username: ')
        username_ulgi='^[a-z0-9_-]{3,15}$'

        check=re.match(username_ulgi,username)
        if check == None:
            print('Durislap kirgizin')
        else:
            print('Username qabillandi')
            break

while True:
        parol=input('Parol: ')
        parol_ulgi='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'

        check=re.match(parol_ulgi,parol)
        if check == None:
            print('Durislap kirgizin')
        else:
            print('Parol qabillandi')
            break
while True:
        phone_number=input('Phone Number: ')
        phone_number_ulgi='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'

        check=re.match(phone_number_ulgi,phone_number)
        if check == None:
            print('Durislap kirgizin')
        else:
            print('Phone Number qabillandi')
            break
while True:
        email_address=input('Email Address: ')
        email_address_ulgi='[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

        check=re.match(email_address_ulgi,email_address)
        if check == None:
            print('Durislap kirgizin')
        else:
            print('Email Address qabillandi')
            break
