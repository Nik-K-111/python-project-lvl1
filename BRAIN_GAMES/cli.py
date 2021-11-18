#! usr/bin/env python3
# docstring

import prompt
# docstring


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
# docstring


def main():
    welcome_user()


if __name__ == '__main__':
    main()
