#! usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.gcd import DESCRIPTION, current_game


def brain_gcd():
    run_game(DESCRIPTION, current_game)


def main():
    brain_gcd()


if __name__ == '__main__':
    main()
