#!/usr/bin/env python

from minesweeper import board


def main():
    b = board.Board()
    b.generate_board(5, 5)
    b.place_mines(5, (0, 0))
    print(b.show_board())


if __name__ == "__main__":
    main()
