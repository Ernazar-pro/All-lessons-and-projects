
x=10
y=7

try:
    z=x/(y-5)
except ZeroDivisionError:
    print('Sandi 0 ge bole almaymiz')
else:
    print(z)