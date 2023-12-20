# Log atli dekorator jaratin,
# ol qaysi funksiya qashan shaqirilganin ham funksiya qashan  tawsilganin waqtin ekranga shigarsin.
# waqtin formatlawdi https://strftime.org/ saytinan koriwiniz mumkin.
#
# Misal:
# @ log
# def hello ():
#   print('hello')

# hello()

# Output:
# - called function: hello at 8:43:35
# hello
# -finished function: hello at 8:43:36

import time
def log(func):
    def inner():
        started= time.strftime('%X',time.gmtime())
        print(started)
        func()
        finished=time.strftime('%X',time.gmtime())
        print(finished)
        
    return inner

@log
def hello():
    time.sleep(3)
    print('Hello')

hello()