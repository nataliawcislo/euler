def ex1(x):
    """
    function which counts the sum of all the multiples of 3 or 5 below x.
    :param x: values
    :return: sum below the x
    """
    sum_of_multiples = 0
    for i in range(1, x):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_multiples += i
    return sum_of_multiples


print(ex1(1000))
