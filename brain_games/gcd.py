#! usr/bin/env python3
# for brain_gcd
# from brain_games.gcd import search_gcd


import prompt
from brain_games.checking import checking
from brain_games.offer import acquaintance
import random


def search_gcd():
    regulations = 'Find the greatest common divisor of given numbeNrs.'
    name = acquaintance(regulations)


    list_1 = [1, 2, 3, 5, 7, 11]
    list_2 = [2, 3, 4, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19]
    base_gcd = (random.sample(list_2, 3))
    i = 3
    while i > 0:
        i -= 1

        n = i
        a1, b1 = (random.sample(list_1, 2))
        a = a1 * base_gcd[n]
        b = b1 * base_gcd[n]
        correct_answer = base_gcd[n]

        print(f'Question: {a} {b} (i={i}, {correct_answer})')
        user_answer = prompt.string('Your answer: ')
        final, i = checking(i, user_answer, correct_answer, name)
        print(f'(i={i}) | {user_answer} | {correct_answer})')

    print(final)


def main():
    search_gcd()


if __name__ == '__main__':
    main()
