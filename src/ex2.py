def ex2(x):
    """
    function which counts the sum values whose not exceed x in the Fibonacci, by starting with 1 and 2.
    :param x: the last number of fibonacci which sets limits
    :return: the sum with below x and have only even-valued
    """
    sum_fibonacci = 0
    i = 1
    j = 2
    how_much = 0
    while sum_fibonacci < x:
        sum_fibonacci = i + j
        if i % 2 == 0:
            how_much += i
        i = j
        j = sum_fibonacci
    return how_much


print(ex2(20))
