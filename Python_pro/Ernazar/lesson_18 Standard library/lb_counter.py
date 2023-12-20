from collections import Counter
from pprint import pprint

with open('saturn.tht') as file:
    text=file.read()


massiv=text.split()

pprint(Counter(massiv)) 