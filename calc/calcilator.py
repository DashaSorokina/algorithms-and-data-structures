#write function calculater() which have string, contains of two integer
#digits and one operation sign +,-,/,* return the result of operation. 
#If given number is not integer or string dont contains sign of operation raise ValueError 

def calculator(expression):
    allowed = '+-/*' 
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Expression should have one sign from ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                if sign =='+':
                    return left+right
                elif sign=='-':
                    return left-right
                elif sign=="*":
                    return left*right
                elif sign == '/':
                    return left/right
            except (ValueError, TypeError):
                raise ValueError('Expression should contains two integer number and one sign')

if __name__=='__main__':
    print(calculator("2+2"))