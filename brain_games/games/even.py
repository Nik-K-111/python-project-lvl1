#  even.py for scripts/brain_even.py

import random
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'


def is_even(number):
    return number % 2 == 0


def current_game():
    question = random.randint(11, 99)

    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
