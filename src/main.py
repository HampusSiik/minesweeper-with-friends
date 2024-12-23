#!/usr/bin/env python

from minesweeper.game.minesweeper import Minesweeper


def main():
    game = Minesweeper()
    game.generate_game(5, 10, 15)
    game.left_click_cell((3, 3))
    print(game._board.show_nearby_mines())


if __name__ == "__main__":
    main()
