def wczytaj_dane(name):
    with open(name, "r") as f:
        data = []
        file = f.read()
        for i in file:
            if i != '\n':
                data.append(int(ord(i) - ord('0')))
    return data


def splitting(x):
    return len(list(map(int, str(x))))


def ex13(x):
    sum = 0
    data = wczytaj_dane("dane_ex13.txt")
    for i in range(0, len(data)):
        if splitting(sum) != x:
            sum += data[i]
        else:
            return sum

print(ex13(2))
