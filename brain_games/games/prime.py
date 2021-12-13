# scripts/brain_prime.py > prime.py

import random
REGULATIONS = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)
ROUNDS = 3


def is_prime(a):
    if a & 1 == 0:
        return False
    d = 3
    while d ** 2 <= a and a % d != 0:
        d += 2
    return d ** 2 > a


def current_game():
    a = random.randint(17, 99)
    if is_prime(a):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = a
    
    return question, correct_answer
