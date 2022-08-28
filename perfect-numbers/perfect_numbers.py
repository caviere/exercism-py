def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    
    asd = 0
    if number > 0:
        for x in range(1, number):
            if (number % x == 0):
                asd += x
               
        if asd == number:
            return 'perfect'
        elif asd > number:
                return 'abundant'
        else:
            return 'deficient'
    else:
        raise ValueError('Classification is only possible for positive numbers.')