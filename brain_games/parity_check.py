#! usr/bin/env python3


import prompt
import random


def parity_check():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no"')

    i = 3
    while i > 0:
        i = i - 1
        proposed_number = random.randint(11, 99)

        if proposed_number & 1 == 1:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

        print('Question: {}'.format(proposed_number))
        user_answer = prompt.string('Your answer: ')
        
        if user_answer == correct_answer:
            result = True
            print('Correct!')

        else:
            result = False
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )

            i = 0

    if result == True:
        print(f"Congratulations, {name}!")


def main():
    parity_check()


if __name__ == '__main__':
    main()
