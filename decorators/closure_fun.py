def add(a,b):
    return a+b

def mull(a,b,c):
    return a*b*c

def closure_with_func(func):
    count = 0
    def inner_fun(*args):
        nonlocal count
        count+=1
        print(f'function {func.__name__} invoked {count} times')
        return func(*args)
    return inner_fun

res = closure_with_func(add)
print(res(10,20))
print(res(19,34))

res2 = closure_with_func(mull)
print(res2(10,20,4))
print(res2(19,34,1))