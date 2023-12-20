# Find Num
import random

def find_num(x=10):
    r_num=random.randint(0,x)
    print(f'Men 0 den {x} qa shekem san oyladim. Buni taba alasanba?')
    urinis=0
    while True:
        int_num=int(input('>>> ')) 
        urinis +=1
        if int_num > r_num:
            print('Kishilew san kirgizin')
        elif int_num < r_num:
            print('Ulkenlew san kirgizin')
        else:
            print('Siz duris taptiniz')
            break
    print(f'{urinis} marte tabiwga urindiniz')
    return urinis

        

def find_num_bot(x=10):
    input(f'Siz 1 den {x} qa shekem san oylan, ham bir knopkani basin. Men tawip koremen >>> ')
    urinis=0
    joqarida= 1
    tomengi= x

    while True:
     urinis +=1
     r_num=random.randint(joqarida,tomengi)
     print(r_num)
     print(f'Menin juwabim  duris bolsa (d), ulken bolsa (-), kishkene bolsa (+)')
     juwap = input('>>> ')
     if juwap == '-':
         joqarida = r_num - 1
     elif juwap == '+':
         joqarida = r_num + 1
     else:
         break
    print(f'Men {urinis} marte tabiwga urindim')
    return urinis

def play(x=10):
    jane=True
    while jane:
        urinis_user = find_num(x)
        urinis_bot = find_num_bot(x)
        if urinis_user < urinis_bot:
            print('Siz uttiniz')
        elif urinis_user > urinis_bot:
            print('Men uttim')
        else:
            print('Tenge ten')
        jane= int(input('Jane oynaymizba? (0/1) >>> '))

play()