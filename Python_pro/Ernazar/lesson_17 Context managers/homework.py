# Log atli kontext menedjer jaratin,
# ol qaysi kontext qashan shaqirilganin ham
# kontext qashan jawilganin waqtin ekranga shigarsin


# Misal :
#
# with log():
#   print("hello")
#
# hello()


# Output:
# - called function: hello at 8:43:35
# hello
# - finished function: hello at 8:43:36

import time
from contextlib import contextmanager

@contextmanager
def log():
    started=time.strftime('%X')
    print(started)
    try:
        yield None
    finally:
        finished=time.strftime('%X')
        print(finished)

with log():
    print("hello")
    time.sleep(3)