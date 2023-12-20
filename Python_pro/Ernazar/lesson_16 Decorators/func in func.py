
def func():
    def another_func():
        return 1
    return another_func

fff=func()
another=fff()

print(another)