def primery_number(number):
    licznik =0
    for dzielnik in range(1, number + 1):
        if number % dzielnik == 0:
            licznik+=1
    if licznik <= 2: return True
    else: return False



def ex7(x):
    list_number = []
    number = 1
    while len(list_number) != x:
        number+=1
        if (primery_number(number)==True):
            list_number.append(number)
    return list_number

print(ex7(15))
