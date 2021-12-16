#  even.py for scripts/brain_even.py

import random


def is_even(number):
    return number % 2 == 0


def current_game():
    DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no"'

    MIN_VALUE, MAX_VALUE = 11, 99

    question = random.randint(MIN_VALUE, MAX_VALUE)

    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return DESCRIPTION, question, correct_answer
