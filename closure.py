# Closure
def everege_numbers():
    numbers = []
    def inner_f(number):
        numbers.append(number)
        return sum(numbers)/len(numbers)
    return inner_f


num1 =  everege_numbers()
num1(2)
num1(8)
num1(9)


# another variant 
def everege_numbers2():
    summa = 0
    count = 0
    def inner_f2(number):
        nonlocal summa
        nonlocal count
        summa+=number 
        count+=1
        return summa/count
    return inner_f2

ever_num =  everege_numbers2()
print(ever_num (2))
print(ever_num (29))
print(ever_num (3))