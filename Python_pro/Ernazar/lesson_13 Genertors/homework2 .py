def float_range(start,stop,step):
    i=start
    while True:
        yield i
        i +=step
        if i == stop:
            break



for i in float_range(0,20,0.5):
    print(i)