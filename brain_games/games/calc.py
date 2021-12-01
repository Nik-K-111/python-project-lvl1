# calc.py for scripts/brain_calc.py


import prompt
import random
from brain_games.offer import acquaintance
from brain_games.checking import checking


def slack_calc():
    regulations = 'What is the result of the expression?'
    name = acquaintance(regulations)

    a_min, a_max = 3, 99
    b_min, b_max = 3, 99
    final = ''
    i = 3
    while i > 0:
        i -= 1
        a = random.randint(a_min, a_max)
        b = random.randint(b_min, b_max)
        sign = random.choice('*-+')
        if sign == "+":
            correct_answer = a + b
        elif sign == "-":
            correct_answer = a - b
        else:
            correct_answer = a * b

        print(f'Question: {a} {sign} {b}')
        user_answer = prompt.integer('Your answer: ')
        final, i = checking(i, user_answer, correct_answer, name)

    print(final)
