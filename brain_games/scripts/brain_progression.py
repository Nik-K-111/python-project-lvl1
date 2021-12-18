#! usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.progression import DESCRIPTION, current_game


def brain_progression():
    run_game(DESCRIPTION, current_game)


def main():
    brain_progression()


if __name__ == '__main__':
    main()
