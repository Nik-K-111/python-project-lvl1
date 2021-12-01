# gcd.py for scripts/brain_gcd.py


import prompt
import random
from brain_games.checking import checking
from brain_games.offer import acquaintance


def search_gcd():
    regulations = 'Find the greatest common divisor of given numbers.'
    name = acquaintance(regulations)
    list_1 = [1, 2, 3, 5, 7, 11]
    list_2 = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
    base_gcd = (random.sample(list_2, 3))

    i = 3
    while i > 0:
        i -= 1
        [a1, b1] = random.sample(list_1, 2)
        a = a1 * base_gcd[i]
        b = b1 * base_gcd[i]
        correct_answer = base_gcd[i]

        print(f'Question: {a} {b}')
        user_answer = prompt.integer('Your answer: ')
        final, i = checking(i, user_answer, correct_answer, name)

    print(final)
