import re

operators = {'plus': '+',
'minus': '-',
'multiplied': '*',
'divided by': '/'}

def clean(question):
    question = re.sub(r'What is', '', question)
    question = re.sub(r'\?', '', question)

    for operator_w, operator_c in operators.items():
        question = re.sub(r'{0}'.format(operator_w), '{0}'.format(operator_c), question)

    power = re.search(r'raised to the ([-]?\d+)th power', question)
    if power:
        question = re.sub(r'raised to the [-]?\d+th power', '** {0}'.format(power.group(1)), question)
    return question.split()

def answer(question):
    cleaned_question = clean(question)
    alien_items = [item for item in cleaned_question if not (item.replace('-', '').isdigit()) and item not in '+-*/']

    if len(cleaned_question) == 0:
        raise ValueError('syntax error')
    if len(alien_items) > 0:
        raise ValueError('unknown operation')

    while len(cleaned_question) > 1:
        try: 
            num1 = int(cleaned_question[0])
            op = cleaned_question[1]
            num2 = int(cleaned_question[2])
        except (ValueError, IndexError) as e:
            raise ValueError('syntax error')

        if op == '+':
            cleaned_question[0:3] = [num1 + num2]
        elif op == '-':
            cleaned_question[0:3] = [num1 - num2]
        elif op == '*':
            cleaned_question[0:3] = [num1 * num2]
        elif op == '/':
            cleaned_question[0:3] = [num1 / num2]
        elif op == '**':
            cleaned_question[0:3] = [num1 ** num2]
    
    return int(cleaned_question[0])
        