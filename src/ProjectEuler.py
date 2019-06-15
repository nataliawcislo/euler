def ex3(x):
    prime_factors = []
    i = 2
    while x != 1:
        while x % i == 0:
            prime_factors.append(i)
            x = x / i
        i += 1
    return prime_factors


#print(ex3(600851475143))

def ex4():
    palin = []

    for i in range(10, 100):
        for i in range(10, 100):
            number = i*i
            size = len(str(number))
            x = [int(k) for k in str(number)]
            if(size%2==0):
                for l in range (0, len(x)/2):
                  for m in range (len(x)-1/2, 0,-1):
                    if(x[l] == x[m]):
                        palin.append(x)
            else:
                for l in range(0, len(x) -1 / 2 ):
                    for m in range(len(x) / 2, 0, -1):
                        if (x[l] == x[m]):
                            palin.append(x)
    return palin


print(ex4())