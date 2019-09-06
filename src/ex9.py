def ex9(x):
    list = []
    for b in range(1, x):
        for c in range(1, x):
            a = x - c - b
            if pythagorean_triplet(a, b, c) == True:
                list.append([a, b, c])
    return list


def pythagorean_triplet(a, b, c):
    if 0<a<b<c:
        if a ** 2 + b ** 2 == c ** 2:
            return True
    else:
        return False


print(ex9(1000))
