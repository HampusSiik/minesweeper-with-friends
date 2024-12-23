#!/usr/bin/env python

from minesweeper.game.minesweeper import Minesweeper


def main():
    game = Minesweeper()
    game.generate_game(5, 10, 10)
    while not game.game_lost() and not game.game_won():
        print(game.get_show_board().show())
        row = int(input("Enter row: "))
        col = int(input("Enter col: "))
        button = input("Enter button: ")
        if button == "l":
            game.left_click_cell((row, col))
        if button == "r":
            game.right_click_cell((row, col))
    print(game._board.show_nearby_mines())


if __name__ == "__main__":
    main()
