from minesweeper.cells.basecell import BaseCell


class EmptyCell(BaseCell):
    """
    Represents an empty cell in the minesweeper game.
    """

    def is_mine(self) -> bool:
        """
        Check if the cell is a mine.

        Returns:
            bool: False
        """
        return False

    def __str__(self) -> str:
        """
        Get the string representation of the cell.

        Returns:
            str: "E"
        """
        return "E"
