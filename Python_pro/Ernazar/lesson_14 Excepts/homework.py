# Kalkulyator programmasin jaratin'
# programma birinshi sandi, ekinshi sandi ha'm artifmetikaliq ameldi input arqali qabilasin

#sanlardi soragan kezde bilmey sozlerdi yamasa hariplerdi jazip algan kezde
#"tek g'ana san jazilsin " degen informatsiya kelsin 
#arifmetiykaliq bilginin ornina basqa zat jazgan kezde da,
#"+, -, /, * belgilernin' birewin kiritin' degen informatsiya kelsin 
while True:
    while True:
        try:
            a=int(input('Birinshi san: '))
            break
        except:
            print('San kiritin')

    while True:
        try:
            b=int(input('Ekinshi san: '))
            break
        except:
            print('San kiritin')

    while True:
        belgi=input('Belgi: ')

        if belgi == '+':
            print(a+b)
            break
        elif belgi == '-':
            print(a-b)
            break
        elif belgi == '*':
            print(a*b)
            break
        elif belgi == '/':
            print(a/b)
            break
        else:
            print('+, -, /, * belgilernin birewin kiritin')