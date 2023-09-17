#some simple example with decorator and how invoke it
def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args,**kwargs)
        print('</table>')
        
    return inner

def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args,**kwargs)
        print('</h1')
        
    return inner

def add_2(a,b):
   print(a+b)

def text():
    print('This is some text for example')

add_2 = table(add_2)
add_2(10,79)

text = header(table(text))
text()





