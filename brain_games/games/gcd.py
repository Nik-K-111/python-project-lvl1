# gcd.py for scripts/brain_gcd.py


import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def which_gcd(a, b):
    a, b = max(a, b), min(a, b)

    while b != 0:
        a, b = b, a % b

    return a


def current_game():
    num_a = random.randint(20, 99)
    num_b = random.randint(20, 99)

    correct_answer = which_gcd(num_a, num_b)
    question = f'{num_a} {num_b}'

    return question, correct_answer
