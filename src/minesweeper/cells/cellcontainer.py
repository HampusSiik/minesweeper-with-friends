from __future__ import annotations

from .cell import Cell
from .minecell import MineCell
from .emptycell import EmptyCell


class CellContainer:
    """
    A container for a cell.
    """

    _cell: Cell
    """
    The cell contained in the container.
    """

    def __init__(self, cell: Cell):
        """
        Initializes a new instance of the CellContainer class containing the
        given cell.

        Args:
            cell (Cell): The cell to wrap.
        """
        self._cell = cell

    def is_mine(self) -> bool:
        """
        Check if the cell is a mine.

        Returns:
            bool: True if the cell is a mine, False otherwise.
        """
        return self._cell.is_mine()

    def is_flagged(self) -> bool:
        """
        Check if the cell is flagged.

        Returns:
            bool: True if the cell is flagged, False otherwise.
        """
        return self._cell.is_flagged()

    def is_revealed(self) -> bool:
        """
        Check if the cell is revealed.

        Returns:
            bool: True if the cell is revealed, False otherwise.
        """
        return self._cell.is_revealed()

    def unwraped(self) -> Cell:
        """
        Unwrap the cell.

        Returns:
            Cell: The unwrapped cell.
        """
        return self._cell.unwraped()

    def flag(self) -> None:
        """
        Flag the cell.
        """
        self._cell = self._cell.flagged()

    def reveal(self) -> None:
        """
        Reveal the cell.
        """
        self._cell = self._cell.revealed()

    def __str__(self) -> str:
        """
        Get the string representation of the cell.

        Returns:
            str: The string representation of the cell.
        """
        return str(self._cell)

    def toggle_flag(self) -> None:
        """
        Toggle the flag of the cell.

        If the cell is flagged, it will be unwrapped. If the cell is not flagged,
        it will be flagged.
        """
        if self.is_flagged():
            self._cell = self._cell.unwraped()
        else:
            self._cell = self._cell.flagged()

    @staticmethod
    def create_mine() -> CellContainer:
        """
        Create a new cell container containing a mine cell.

        Returns:
            CellContainer: A new cell container containing a mine cell.
        """
        return CellContainer(MineCell())

    @staticmethod
    def create_empty() -> CellContainer:
        """
        Create a new cell container containing an empty cell.

        Returns:
            CellContainer: A new cell container containing an empty cell.
        """
        return CellContainer(EmptyCell())
