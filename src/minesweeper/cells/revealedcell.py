from minesweeper.cells.cell import Cell


class RevealedCell:
    """
    Represents a revealed cell in the minesweeper game.
    """

    _cell: Cell
    """
    The revealed cell.
    """

    def __init__(self, cell: Cell):
        """
        Initializes a new instance of the RevealedCell class containing the given cell.

        Args:
            cell (Cell): The cell to reveal.
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
        return self._cell.flagged()

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
