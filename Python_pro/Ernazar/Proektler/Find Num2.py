jane=True
while jane:
    print('Qalegen san oylan')
    input('San oylan: ')


    input('Soni sogan qos, 1=qostim: ')

    input('Kiynen soni 2 ge kobeyt, 2=kobeyttim: ')

    input('Kiynen oylagan sanindi shiqqan sanga bol: ')
    input('Senin juwabin 4 shiqti, durispa? 4=awa, 5=yaq: ')


    jane= int(input('Jane oynaymizba? (0/1) >>> '))

import random

jane=True

while jane:
    input('Qalegen san oyla')
    a=random.randint(2,5)
    input('Soni sogan qos')
    input(f'Kiynen soni {a} ga kobeyt')
    input('Shiqqan sanindi oylagan sanga bol')
    print(f'{a*2}')
    jane= int(input('Jane oynaymizba (0/1) >>> '))

