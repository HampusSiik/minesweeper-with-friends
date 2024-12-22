from minesweeper.cells.cell import Cell


class FlaggedCell:
    """
    Represents a flagged cell in the minesweeper game.
    """

    _cell: Cell
    """
    The flagged cell.
    """

    def __init__(self, cell: Cell):
        """
        Initializes a new instance of the FlaggedCell class containing the given cell.

        Args:
            cell (Cell): The cell to flag.
        """
        self._cell = cell

    def is_mine(self) -> bool:
        """
        Check if the cell is a mine.

        Returns:
            bool: True if the cell is a mine, False otherwise
        """
        return self._cell.is_mine()

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

    def unwraped(self) -> Cell:
        """
        Unwrap the cell.

        Returns:
            Cell: The unwrapped cell.
        """
        return self._cell.unwraped()

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
        return self._cell.revealed()

    def __str__(self) -> str:
        """
        String representation of the cell.

        Returns:
            str: "F"
        """
        return "F"
