def ex3(x):
    prime_factors = []
    i = 2
    while x != 1:
        while x % i == 0:
            prime_factors.append(i)
            x = x / i
        i += 1
    return prime_factors


print(ex3(600851475143))
