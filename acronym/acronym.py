import re

def abbreviate(words):
    return ''.join([word.upper()[0] for word in re.sub('[-_]', '', words).split()])
