plain = 'abcdefghijklimnopqrstuvwxyz'
cipher = 'zyxwvutsrqponmilkjihgfedcba'

def cleanup(text):
    return ''.join(a.lower() for a in text if a.isalnum())

def encode(plain_text):
    text = cleanup(text)
    text = text.translate(text.maketrans(plain, cipher))
    return ''.join(text[i:i+5] for i in range(0, len(text), 5))


def decode(ciphered_text):
    return ciphered_text.translate(ciphered_text.maketrans(plain, cipher)).replace('', '')
