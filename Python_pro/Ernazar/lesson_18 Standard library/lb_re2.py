import re
#ihateregex.io

text='My name is Aybek, my surname is Jumashev. My phone number is +98293848755. My email adress is aybek.djumashev@gmail.com' 

email_ulgi='[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

#print(re.findall(email_ulgi,text))


tel_ulgi='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
tel_number='+98293848755'

#print(re.match(tel_ulgi,tel_number))


while True:
    parol=input('Parol: ')
    parol_ulgi='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'

    check=re.match(parol_ulgi,parol)
    if check == None:
        print('Durislap kirgizin')
    else:
        print('Parol qabillandi')
        break
