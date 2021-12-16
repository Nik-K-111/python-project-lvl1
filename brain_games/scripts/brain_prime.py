#! usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.prime import current_game


def brain_prime():
    run_game(current_game)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
