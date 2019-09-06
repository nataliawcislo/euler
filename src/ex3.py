def ex3(x):
    '''
    function which break down the number into prime numbers, and return max element with list
    :param x: the number we break down into prime numbers
    :return: max prime numbers
    '''
    prime_factors = []
    i = 2
    while x != 1:
        while x % i == 0:
            prime_factors.append(i)
            x = x / i
        i += 1
    return max(prime_factors)


print(ex3(600851475143))
