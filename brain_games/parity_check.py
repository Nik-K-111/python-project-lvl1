#! usr/bin/env python3

import prompt
import random
from brain_games.offer import acquaintance
from brain_games.checking import checking

def parity_check():
    regulations = 'Answer "yes" if the number is even, otherwise answer "no"'
    name = acquaintance(regulations)

    # Определение значений, запуск цикла задач.
    a_min, a_max = 11, 99
    final = ''
    i = 3
    while i > 0:
        i -= 1
        a = random.randint(a_min, a_max)
        if a & 1 == 1:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        print(f'Question: {a}')
        user_answer = prompt.string('Your answer: ')
        final, i = checking(i, user_answer, correct_answer, name)

    print(final)


def main():
    parity_check()


if __name__ == '__main__':
    main()
