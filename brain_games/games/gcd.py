# gcd.py for scripts/brain_gcd.py


import random

REGULATIONS = 'Find the greatest common divisor of given numbers.'
ROUNDS = 3


def current_game():

    list_1 = [1, 2, 3, 5, 7, 11]
    list_2 = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
    [base_gcd] = (random.sample(list_2, 1))
    [a1, b1] = random.sample(list_1, 2)
    a = a1 * base_gcd
    b = b1 * base_gcd
    correct_answer = base_gcd
    question = f'{a} {b}'

    return question, correct_answer
