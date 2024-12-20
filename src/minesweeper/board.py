from typing import List, Tuple, Generator
import random

from minesweeper.cells.cellcontainer import CellContainer

Position = Tuple[int, int]

class Board:
    """
    Minesweeper board.
    """

    _board: List[List[CellContainer]]

    def __init__(self):
        """
        Initialize the board.
        """
        self._board = [[]]

    def generate_board(self, width: int, height: int) -> None:
        """
        Generate an empty board with the given dimensions.

        Args:
            width (int): Width of the board.
            height (int): Height of the board.
        """
        self._board = [[CellContainer.create_empty() for _ in range(width)] for _ in range(height)]

    def place_mines(self, mines: int, start_position: Position) -> None:
        """
        Place mines on the board.

        Does not place mines on the start position.

        Does not avoid existing mines.

        Args:
            mines (int): Number of mines to place.
            start_position (Position): Position where the first cell was clicked.
        """
        positions = [(x, y) for x in range(len(self._board)) for y in range(len(self._board[0]))]
        positions.remove(start_position)
        mines_positions = random.sample(positions, mines)
        for x, y in mines_positions:
            self._board[x][y] = CellContainer.create_mine()

    def show_board(self) -> str:
        """
        String representation of the board.

        Returns:
            str: String representation of the board.
        """
        return "\n".join(["".join([str(cell.unwraped()) for cell in row]) for row in self._board])

    def surrounding_mines(self, position: Position) -> int:
        """
        Number of mines surrounding a position.

        Args:
            position (Position): Position to check.
        Returns:
            int: Number of mines surrounding the position.
        """
        return sum([self._board[i][j].is_mine() for i, j in self._bounded_range(position)])

    def _bounded_range(self, position: Position) -> Generator[Position]:
        """
        Range of positions around position that are within the board.

        Args:
            position (Position): Position to get the range around.
        Returns:
            Generator[Position]: List of positions around position that are within the board.
        """
        x, y = position
        return ((i, j) for i in range(max(0, x - 1), min(len(self._board), x + 2)) for j in range(max(0, y - 1), min(len(self._board[0]), y + 2)))
