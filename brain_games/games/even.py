#  even.py for scripts/brain_even.py

import random

REGULATIONS = 'Answer "yes" if the number is even, otherwise answer "no"'
ROUNDS = 3


def is_even(number):
    if number & 1 == 1:
        return False
    return True


def current_game():

    MIN_VALUE, MAX_VALUE = 11, 99

    question = random.randint(MIN_VALUE, MAX_VALUE)

    if is_even(question):
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    return question, correct_answer
