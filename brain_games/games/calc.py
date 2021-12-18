# calc.py for scripts/brain_calc.py

import random

DESCRIPTION = 'What is the result of the expression?'


def arithmetic(a, b, operator):
    if operator == '+':
        expression = f'{a} + {b}'
        result = a + b
    elif operator == '-':
        a, b = max(a, b), min(a, b)
        expression = f'{a} - {b}'
        result = a - b
    elif operator == '*':
        expression = f'{a} * {b}'
        result = a * b

    return expression, result


def current_game():
    list_operators = ['+', '-', '*']
    num_a = random.randint(3, 99)
    num_b = random.randint(3, 99)
    operator = random.choice(list_operators)

    question, correct_answer = arithmetic(num_a, num_b, operator)

    return question, correct_answer
