# scripts/brain_prime.py > prime.py

import random


def is_prime(a):
    if a % 2 == 0:
        return False
    d = 3
    while d ** 2 <= a and a % d != 0:
        d += 2
    return d ** 2 > a


def current_game():
    DESCRIPTION = (
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )

    MIN_VALUE, MAX_VALUE = 17, 99

    num = random.randint(MIN_VALUE, MAX_VALUE)
    if is_prime(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = num

    return DESCRIPTION, question, correct_answer
