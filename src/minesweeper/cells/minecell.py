from minesweeper.cells.basecell import BaseCell


class MineCell(BaseCell):
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

    def __str__(self) -> str:
        """
        Get the string representation of the cell.

        Returns:
            str: "M"
        """
        return "M"
