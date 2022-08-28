def convert(number):
    factors = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    outcome = ''
    for key, value in factors.items():
        if number % key == 0:
            outcome += value
    return outcome or str(number)
