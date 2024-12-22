from minesweeper.cells.cell import Cell
from minesweeper.cells.flaggedcell import FlaggedCell
from minesweeper.cells.revealedcell import RevealedCell


class MineCell:
    """
    Represents a mine cell in the minesweeper game.
    """

    def is_mine(self) -> bool:
        """
        Check if the cell is a mine.

        Returns:
            bool: True
        """
        return True

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

    def __str__(self) -> str:
        """
        Get the string representation of the cell.

        Returns:
            str: "M"
        """
        return "M"
