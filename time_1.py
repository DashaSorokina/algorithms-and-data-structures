from datetime import datetime
from time import perf_counter

def timer():
    start = datetime.now()

    def inner():
        return datetime.now() - start
    
    return inner

duration = timer()
print(duration())
print(duration())
print(duration())


def timer():
    start = datetime.now()

    def inner():
        return datetime.now() - start
    
    return inner


def time2():
    start = perf_counter()

    def inner2():
        return perf_counter() - start
    
    return inner2



def time3():
    start = perf_counter()

    def inner3():
        nonlocal start  # Use the start variable from the outer function
        current = perf_counter()
        elapsed = current - start
        start = current  # Update the start time for the next call
        return elapsed
    
    return inner3

duration3 = time3()
print(duration3())  
print(duration3())  
print(duration3())  