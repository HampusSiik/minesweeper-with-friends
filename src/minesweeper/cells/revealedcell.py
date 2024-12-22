from minesweeper.cells.cell import Cell
from minesweeper.cells.cellwraper import CellWrapper


class RevealedCell(CellWrapper):
    """
    Represents a revealed cell in the minesweeper game.
    """

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
            bool: True
        """
        return True

    def flagged(self) -> Cell:
        """
        Flag the cell.

        Returns:
            Cell: The contained cell flagged.
        """
        return self.unwraped().flagged()

    def revealed(self) -> Cell:
        """
        Reveal the cell.

        Returns:
            Cell: The contained cell revealed.
        """
        return self

    def __str__(self) -> str:
        """
        String representation of the cell.

        Returns:
            str: "R"
        """
        return "R"
