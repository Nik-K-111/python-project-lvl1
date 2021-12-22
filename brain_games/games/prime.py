# scripts/brain_prime.py > prime.py

import random

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(a):
    d = a ** 0.5 + 1
    i = 2
    while i <= d and a % i != 0:
        i += 1
    return i ** 2 > a


def generate_round():
    question = random.randint(17, 99)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return DESCRIPTION, question, correct_answer
