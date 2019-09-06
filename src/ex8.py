def wczytaj_dane(name):
    with open(name, "r") as f:
        data = []
        file = f.read()
        for i in file:
            if i != '\n':
                data.append(int(ord(i) - ord('0')))
    return data


def ex8(size):
    data = wczytaj_dane("dane.txt")
    limit = []
    max_value = 0
    temp_value = 0
    for i in range(0, size):
        limit.append(data[i])
    for i in range(0, len(data) - size):
        temp_value = sum(limit)
        if (temp_value > max_value):
             max_value = temp_value
        if (len(data) != 0):
            limit.pop(0)
            limit.append(data[size+i])
    return max_value


print(ex8(4))
