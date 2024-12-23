#!/usr/bin/env python

from minesweeper.game.minesweeper import Minesweeper


def main():
    game = Minesweeper()
    game.generate_board(5, 10)
    game.place_mines(15, (3, 3))
    print(game._board.show_nearby_mines())


if __name__ == "__main__":
    main()
