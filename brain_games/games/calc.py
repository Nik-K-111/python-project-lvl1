# calc.py for scripts/brain_calc.py

import random

DESCRIPTION = 'What is the result of the expression?'


def calc(a, b, operator):
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    return result

def generate_round():
    list_operators = ['+', '-', '*']
    num_a = random.randint(3, 99)
    num_b = random.randint(3, 99)
    operator = random.choice(list_operators)
    question = f'{num_a} {operator} {num_b}'

    correct_answer = calc(num_a, num_b, operator)

    return DESCRIPTION, question, correct_answer
