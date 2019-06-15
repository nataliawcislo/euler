def ex4():
    palin = []

    for i in range(10, 100):
        for j in range(10, 100):
            number = i * j
            size = len(str(number))
            x = [int(k) for k in str(number)]
            if size % 2 == 0:
                for l in range(0, len(x) / 2):
                    for m in range(len(x) - 1 / 2, 0, -1):
                        if x[l] == x[m]:
                            palin.append(x)
            else:
                for l in range(0, len(x) - 1 / 2):
                    for m in range(len(x) - 1, 0, -2 / 2):
                        if x[l] == x[m]:
                            palin.append(x)
    return palin


print(ex4())
