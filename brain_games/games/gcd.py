# gcd.py for scripts/brain_gcd.py


import random


def current_game():
    DESCRIPTION = 'Find the greatest common divisor of given numbers.'

    MIN_VALUE_GCD, MAX_VALUE_GCD = 2, 15
    LIST_QUOTIENT = [2, 3, 5, 7, 11, 13, 17, 19]

    gcd = random.randint(MIN_VALUE_GCD, MAX_VALUE_GCD)
    [quotient_a, quotient_b] = random.sample(LIST_QUOTIENT, 2)
    a = quotient_a * gcd
    b = quotient_b * gcd
    correct_answer = gcd
    question = f'{a} {b}'

    return DESCRIPTION, question, correct_answer
