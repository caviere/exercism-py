def _rotate(text):
    return text[1:] + text[0]


def translate(text):
    if text[:2] == 'xr':
        return 'xrayay'
    if text[0] == 'y' and text[1] in 'aeiou':
        text = _rotate(text)
    while text[0] not in 'aeiouy':
        text = _rotate(text)
    if text[-1] == 'q' and text[0] == 'u':
        text = _rotate(text)
    return text + 'ay' 
