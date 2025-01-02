from abc import ABC, abstractmethod

from .basecell import Cell


class CellWrapper(ABC):
    """
    Represents a cell wrapper in the minesweeper game.
    """

    _cell: Cell
    """
    The wrapped cell.
    """

    def __init__(self, cell: Cell):
        """
        Initializes a new instance of the CellWrapper class containing the given cell.

        Args:
            cell (Cell): The cell to wrap.
        """
        self._cell = cell

    def is_mine(self) -> bool:
        """
        Check if the cell is a mine.

        Returns:
            bool: True if the cell is a mine, False otherwise
        """
        return self._cell.is_mine()

    def unwraped(self) -> Cell:
        """
        Unwrap the cell.

        Returns:
            Cell: The unwrapped cell.
        """
        return self._cell.unwraped()

    @abstractmethod
    def is_flagged(self) -> bool:
        """
        Check if the cell is flagged.

        Returns:
            bool: False
        """
        pass

    @abstractmethod
    def is_revealed(self) -> bool:
        """
        Check if the cell is revealed.

        Returns:
            bool: True
        """
        pass

    @abstractmethod
    def flagged(self) -> Cell:
        """
        Flag the cell.

        Returns:
            Cell: The contained cell flagged.
        """
        pass

    @abstractmethod
    def revealed(self) -> Cell:
        """
        Reveal the cell.

        Returns:
            Cell: The contained cell revealed.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        String representation of the cell.

        Returns:
            str: "F" for flagged cell, "R" for revealed cell
        """
        pass
