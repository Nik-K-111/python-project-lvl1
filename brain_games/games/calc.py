import random

DESCRIPTION = 'What is the result of the expression?'


def calc(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    else:
        None


def generate_round():
    operations = ['+', '-', '*']
    num_a = random.randint(3, 99)
    num_b = random.randint(3, 99)
    operator = random.choice(operations)
    question = f'{num_a} {operator} {num_b}'

    result = calc(num_a, num_b, operator)

    return question, result
