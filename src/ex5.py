def ex5(number):
    how_divided = 1  # type: int
    for i in range(2, 21):
        if(number%i==0):
            how_divided+=1
    if(how_divided==20):
        return number
    else:
        return "can't be divided "


print(ex5(2520))