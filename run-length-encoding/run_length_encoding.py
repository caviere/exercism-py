def decode(string):
    decoded = ''
    count = []
    
    for x in string:
        if x.isdigit():
            count.append(x)
            continue
        if len(count) == 0:
            count = ["1"]
            decoded += x * int("".join(count))
            
        count = []
    
    return decoded

        
def encode(string):
    if not string:
        return string

    encoded = ''
    count = 0
    current = string[0]
    
    for x in string:
        if x == current:
            count += 1
            continue
        if count > 1:
            encoded += str(count)
        
        encoded += current
        current = x
        count = 1
    else:
        if count > 1:
            encoded += str(count)
        
        encoded += current

    return encoded
