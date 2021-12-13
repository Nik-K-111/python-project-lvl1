# calc.py for scripts/brain_calc.py

import random

REGULATIONS = 'What is the result of the expression?'
ROUNDS = 3


def current_game():

    A_MIN_VALUE, A_MAX_VALUE = 3, 99
    B_MIN_VALUE, B_MAX_VALUE = 3, 99
    
    a = random.randint(A_MIN_VALUE, A_MAX_VALUE)
    b = random.randint(B_MIN_VALUE, B_MAX_VALUE)
    sign = random.choice('*-+')
    
    if sign == "+":
        correct_answer = a + b
    elif sign == "-":
        correct_answer = a - b
    else:
        correct_answer = a * b

    question = f'{a} {sign} {b}'
    
    return question, correct_answer
