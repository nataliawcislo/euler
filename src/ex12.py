def ex12(x):
    i = 1
    licznik = False
    while licznik != True:
        if divisor(triangle(i)) == x+1:
            licznik = True
        else:
            i += 1
    return triangle(i)

def triangle(x):
    value = x * (x + 1) / 2
    return value


def divisor(x):
    list = []
    for i in range(1, x+1):
        if x % i == 0:
            list.append(i)
    return len(list)

print(ex12(10))
