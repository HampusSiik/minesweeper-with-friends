from typing import Tuple
from minesweeper.position import Position
from minesweeper.board import board


class Minesweeper:
    def __init__(self):
        self.board = board.Board()

    def shape(self) -> Tuple[int, int]:
        return self.board.shape()

    def game_lost(self) -> bool:
        return any(
            self.board.is_mine(position) and self.board.is_revealed(position)
            for position in self.board.all_positions()
        )

    def game_won(self) -> bool:
        return (
            all(
                self.board.is_mine(position) or self.board.is_revealed(position)
                for position in self.board.all_positions()
            )
            and not self.game_lost()
        )

    def left_click_cell(self, position: Position) -> None:
        if self.board.is_flagged(position):
            return
        self.board.reveal(position)

    def right_click_cell(self, position: Position) -> None:
        if self.board.is_revealed(position):
            return
        self.board.toggle_flag(position)

    def generate_board(self, rows: int, columns: int) -> None:
        self.board.generate_board(rows, columns)

    def place_mines(self, num_mines: int, position: Position) -> None:
        self.board.place_mines(num_mines, position)
