from typing import List, Tuple
import random

from minesweeper.cells.cellcontainer import CellContainer



class Board:

    _board: List[List[CellContainer]]

    def __init__(self):
        self._board = [[]]

    def generate_board(self, width: int, height: int) -> None:
        self._board = [[CellContainer.create_empty() for _ in range(width)] for _ in range(height)]

    def place_mines(self, mines: int, start_position: Tuple[int, int]) -> None:
        positions = [(x, y) for x in range(len(self._board)) for y in range(len(self._board[0]))]
        positions.remove(start_position)
        mines_positions = random.sample(positions, mines)
        for x, y in mines_positions:
            self._board[x][y] = CellContainer.create_mine()

    def show_board(self) -> str:
        return "\n".join(["".join([str(cell.unwraped()) for cell in row]) for row in self._board])
