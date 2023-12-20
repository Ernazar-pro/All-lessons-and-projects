
def adder(n):
    def inner(m):
        return n+m
    return inner

add= adder(5)
result=add(3)


print(result)