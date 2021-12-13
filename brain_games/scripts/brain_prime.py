#! usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.prime import REGULATIONS, ROUNDS, current_game


def brain_prime():
    run_game(REGULATIONS, ROUNDS, current_game)


def main():
    brain_prime()


if __name__ == '__main__':
    main()
