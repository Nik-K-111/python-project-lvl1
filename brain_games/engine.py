# engine.py - Движок игры

import prompt


def run_game(DESCRIPTION, current_game):
    # description = DESCRIPTION
    ROUNDS = 3

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print(
        f'Hello, {name}!\n'
        f'{DESCRIPTION}'
    )

    for i in range(ROUNDS):
        question, correct_answer = current_game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(correct_answer):
            print('Correct!')
            final = (f"Congratulations, {name}!")
        else:
            final = (
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    print(final)
