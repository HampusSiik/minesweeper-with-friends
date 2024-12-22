from typing import List, Tuple, Generator
import random

from minesweeper.cells.cellcontainer import CellContainer

Position = Tuple[int, int]


class Board:
    """
    Minesweeper board.
    """

    _board: List[List[CellContainer]]
    """
    List of lists of CellContainers.
    """

    def __init__(self):
        """
        Initialize the board.
        """
        self._board = [[]]

    def generate_board(self, rows: int, cols: int) -> None:
        """
        Generate an empty board with the given dimensions.

        Args:
            rows (int): Width of the board.
            cols (int): Height of the board.
        """
        self._board = [
            [CellContainer.create_empty() for _ in range(cols)] for _ in range(rows)
        ]

    def get_board(self) -> List[List[CellContainer]]:
        """
        Get the board.

        Returns:
            List[List[CellContainer]]: The board.
        """
        return self._board

    def shape(self) -> Tuple[int, int]:
        """
        Get the shape of the board.

        Returns:
            Tuple[int, int]: Shape of the board.
        """
        return len(self._board), len(self._board[0])

    def place_mines(self, mines: int, start_position: Position) -> None:
        """
        Place mines on the board.

        Does not place mines on the start position.

        Does not avoid existing mines.

        Args:
            mines (int): Number of mines to place.
            start_position (Position): Position where the first cell was clicked.
        """
        positions = [
            (x, y) for x in range(len(self._board)) for y in range(len(self._board[0]))
        ]
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
        return "\n".join(["".join([str(cell) for cell in row]) for row in self._board])

    def surrounding_mines(self, position: Position) -> int:
        """
        Number of mines surrounding a position.

        Args:
            position (Position): Position to check.
        Returns:
            int: Number of mines surrounding the position.
        """
        return sum(
            [self._board[i][j].is_mine() for i, j in self._bounded_range(position)]
        )

    def _bounded_range(self, position: Position) -> Generator[Position]:
        """
        Range of positions around position that are within the board.

        Args:
            position (Position): Position to get the range around.
        Returns:
            Generator[Position]: List of positions around position that are within the board.
        """
        x, y = position
        return (
            (i, j)
            for i in range(max(0, x - 1), min(len(self._board), x + 2))
            for j in range(max(0, y - 1), min(len(self._board[0]), y + 2))
        )

    def show_nearby_mines(self) -> str:
        """
        String representation of the board with the number of mines around each cell.
        And mines are represented by '*'.

        Args:
            position (Position): Position to check.
        Returns:
            str: String representation of the board with the number of mines around each cell.
        """
        return "\n".join(
            self._show_nearby_mines_row(i) for i in range(len(self._board))
        )

    def _show_nearby_mines_cell(self, position: Position) -> str:
        """
        String representation of a single cell. If the cell is a mine, it returns '*'.
        Otherwise, it returns the number of surrounding mines.

        Args:
            position (Position): Position to check.
        Returns:
            str: String representation of the cell.
        """
        x, y = position
        return (
            "*"
            if self._board[x][y].is_mine()
            else str(self.surrounding_mines(position))
        )

    def _show_nearby_mines_row(self, row: int) -> str:
        """
        String representation of a row of cells. If the cell is a mine, it returns '*'.
        Otherwise, it returns the number of surrounding mines.

        Args:
            row int: Row number of the row to check.
        Returns:
            str: String representation of the row.
        """
        return "".join(
            self._show_nearby_mines_cell((row, i)) for i in range(len(self._board[row]))
        )
