# Generators

def counter():
    a=42
    yield a

    b=21
    yield b

    c=34
    yield c

for a in counter():
    print(a)
