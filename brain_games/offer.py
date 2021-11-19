#! usr/bin/env python3

# offer.py - Знакомство, предложение сыграть, правила.
# 1 аргумент: regulations
# 1 результат: name


import prompt



def acquaintance(regulations):
    print(f'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        f'Hello, {name}!\n'
        f'{regulations}'
    )

    return name
