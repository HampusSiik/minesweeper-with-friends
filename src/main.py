#!/usr/bin/env python

from minesweeper.game.minesweeper import Minesweeper


def main():
    game = Minesweeper()
    game.generate_game(5, 10, 15)
    game.left_click_cell((3, 3))
    print(game.get_show_board().show())


if __name__ == "__main__":
    main()
