def ex6(number1, number2):
    n1 = square_of_the_sum(number1)
    n2 = squares_of_the_first(number2)
    return n1-n2

def squares_of_the_first(number):
    sum = 0
    for i in range(0, number+1):
        sum +=i ** 2
    return sum

def square_of_the_sum(number):
    sum = 0
    for i in range(0, number+1):
        sum +=i
    squer=sum**2
    return squer
    
print(ex6(10,10))