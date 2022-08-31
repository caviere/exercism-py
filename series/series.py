def slices(series, length):
    if length == 0:
        raise ValueError('slice length cannot be zero')
    if length < 0:
        raise ValueError('slice length cannot be negative')
    if len(series) == 0:
        raise ValueError('series cannot be empty')
    if length > len(series):
        raise ValueError('slice length cannot be greater than series length')

    sequence = []
    i = 0
    while i + length <= len(series):
        sequence.append(series[i:i+length])
        i += 1
    return sequence