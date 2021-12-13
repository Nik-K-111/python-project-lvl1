# engine.py - Движок игры

import prompt


def run_game(REGULATIONS, ROUNDS, current_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        f'Hello, {name}!\n'
        f'{REGULATIONS}'
    )
    while ROUNDS > 0:
        ROUNDS -= 1
        question, correct_answer = current_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(correct_answer):
            print('Correct!')
            final = (f"Congratulations, {name}!")
        else:
            ROUNDS = 0
            final = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
    print(final)
