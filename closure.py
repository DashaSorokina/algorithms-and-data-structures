# Замыкание 
def everege_numbers():
    numbers = []
    def inner_f(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers)/len(numbers)
    return inner_f


num1 =  everege_numbers()
num1(2)
num1(8)
num1(9)
