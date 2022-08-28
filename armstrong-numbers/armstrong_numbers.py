def is_armstrong_number(number):
    len_number = len(str(number))
    return number == sum(int(value) ** len_number for value in str(number))
