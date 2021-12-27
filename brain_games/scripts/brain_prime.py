#! usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games import prime
game = prime


def main():
    run_game(game)


if __name__ == '__main__':
    main()
