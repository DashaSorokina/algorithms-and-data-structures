from functools import wraps
#different syntaxis for decorators  + wrapp decorator
def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
    inner.__name__ = func.__name__ #idea: we can change name of inner function on name from originak func
    inner.__doc__ = func.__doc__
    return inner

def header(func):
    @wraps(func)  #as argument put in wrapp function, which we want to decorate (original func)
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args,**kwargs)
        print('</h1')
        
    return inner

@table
def add_2(a,b):
   '''
   This function adding two numbers
   :params a:
   :params b:
   :return:
   '''
   print(a+b)


@header
@table
def text():
    '''
    print some text
    :return:
    '''
    print('This is some text for example')

#The problem: when we ggive function to inner function, our original function losse 
#her name and commets, to solve this we can use magic f.__name__, and @wrapp decorator
#f.__doc__ save all comment and documentations


add_2(10,79)
print('name of decorated function: ',add_2.__name__)
print(add_2.__doc__)

text()
print('name of decorated function: ', text.__name__)
print(text.__doc__)
