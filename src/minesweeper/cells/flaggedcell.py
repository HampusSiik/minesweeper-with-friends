from .cell import Cell
from .cellwraper import CellWrapper


class FlaggedCell(CellWrapper):
    """
    Represents a flagged cell in the minesweeper game.
    """

    def is_flagged(self) -> bool:
        """
        Check if the cell is flagged.

        Returns:
            bool: True
        """
        return True

    def is_revealed(self) -> bool:
        """
        Check if the cell is revealed.

        Returns:
            bool: False
        """
        return False

    def flagged(self) -> Cell:
        """
        Flag the cell.

        Returns:
            Cell: The contained cell flagged.
        """
        return self

    def revealed(self) -> Cell:
        """
        Reveal the cell.

        Returns:
            Cell: The contained cell revealed.
        """
        return self.unwraped().revealed()

    def __str__(self) -> str:
        """
        String representation of the cell.

        Returns:
            str: "F"
        """
        return "F"
