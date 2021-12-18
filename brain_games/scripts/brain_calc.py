#! usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.calc import DESCRIPTION, current_game


def brain_calc():
    run_game(DESCRIPTION, current_game)


def main():
    brain_calc()


if __name__ == '__main__':
    main()
