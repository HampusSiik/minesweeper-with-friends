from abc import ABC, abstractmethod

from .cell import Cell
from .revealedcell import RevealedCell
from .flaggedcell import FlaggedCell


class BaseCell(ABC):
    """
    Represents a cell in the minesweeper game.
    """

    @abstractmethod
    def is_mine(self) -> bool:
        """
        Check if the cell is a mine.

        Returns:
            bool: True if the cell is a mine, False otherwise
        """
        pass

    def is_flagged(self) -> bool:
        """
        Check if the cell is flagged.

        Returns:
            bool: False
        """
        return False

    def is_revealed(self) -> bool:
        """
        Check if the cell is revealed.

        Returns:
            bool: False
        """
        return False

    def unwraped(self) -> Cell:
        """
        Unwrap the cell.

        Returns:
            Cell: self.
        """
        return self

    def flagged(self) -> Cell:
        """
        Flag the cell.

        Returns:
            Cell: The cell flagged.
        """
        return FlaggedCell(self)

    def revealed(self) -> Cell:
        """
        Reveal the cell.

        Returns:
            Cell: The cell revealed.
        """
        return RevealedCell(self)

    @abstractmethod
    def __str__(self) -> str:
        """
        Get the string representation of the cell.

        Returns:
            str: "M" for mines and "E" for empty cells.
        """
        pass
