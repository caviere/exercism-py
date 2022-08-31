import math

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    if number < 1:
        raise ValueError('input must be 1 or greater')
    count = 2
    prime_count = 0
    while True:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            prime_count += 1
        if prime_count == number:
            return count
            break 
        count += 1

