def org_range(n):
    i=0
    while True:
        yield i
        i +=1
        if i == n:
            break



for i in org_range(10000000000000):
    print(i)