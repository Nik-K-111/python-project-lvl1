# offer.py - Знакомство, предложение сыграть, правила.


import prompt


def acquaintance(regulations):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        f'Hello, {name}!\n'
        f'{regulations}'
    )

    return name
