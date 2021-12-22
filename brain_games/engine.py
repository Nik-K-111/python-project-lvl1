# engine.py - Движок игры

import prompt

ROUNDS = 3


def run_game(generate_round):
    description, *z = generate_round()

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')

    print(
        f'Hello, {name}!\n'
        f'{description}'
    )

    for i in range(ROUNDS):
        *z, question, correct_answer = generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if str(user_answer) == str(correct_answer):
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return
    print(f"Congratulations, {name}!")
