import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    num_a = random.randint(20, 99)
    num_b = random.randint(20, 99)
    question = f'{num_a} {num_b}'
    correct_answer = gcd(num_a, num_b)

    return question, correct_answer
