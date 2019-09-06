def primery_number(number):
    licznik =0
    for dzielnik in range(1, number + 1):
        if number % dzielnik == 0:
            licznik+=1
    if licznik <= 2: return True
    else: return False



def ex10(x):
    list_number = []
    number = 1
    while  number < x:
        number+=1
        if (primery_number(number)==True):
            list_number.append(number)
    return sum(list_number)

print(ex10(10))
