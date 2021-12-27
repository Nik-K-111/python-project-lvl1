# scripts/brain_prime.py > prime.py

import random

DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(a):
    d = round(a ** 0.5 + 1)
    for i in range(2, d):
        if a % i == 0:
            return False
    return True


def generate_round():
    question = random.randint(13, 99)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
