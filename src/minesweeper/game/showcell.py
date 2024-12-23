from typing import Optional


class ShowCell:
    """
    Cell with revealed information.
    """

    _adjacent_mines: Optional[int]
    """
    Number of adjacent mines.
    """

    _is_mine: Optional[bool]
    """
    Whether the cell is a mine.
    """

    _is_flagged: bool
    """
    Whether the cell is flagged.
    """

    _is_revealed: bool
    """
    Whether the cell is revealed.
    """

    def __init__(
        self,
        adjacent_mines: Optional[int],
        is_mine: Optional[bool],
        is_flagged: bool,
        is_revealed: bool,
    ):
        """
        Initialize the cell.

        Args:
            adjacent_mines (Optional[int]): Number of adjacent mines.
            is_mine (Optional[bool]): Whether the cell is a mine.
            is_flagged (bool): Whether the cell is flagged.
            is_revealed (bool): Whether the cell is revealed.
        """
        self._adjacent_mines = adjacent_mines
        self._is_mine = is_mine
        self._is_flagged = is_flagged
        self._is_revealed = is_revealed

    def adjacent_mines(self) -> Optional[int]:
        """
        Get the number of adjacent mines.

        Returns:
            int: Number of adjacent mines. None if the cell is not revealed.
        """
        return self._adjacent_mines

    def is_mine(self) -> Optional[bool]:
        """
        Check if a cell is a mine.

        Returns:
            bool: True if the cell is a mine, False otherwise. None if the cell is not revealed.
        """
        return self._is_mine

    def is_flagged(self) -> bool:
        """
        Check if a cell is flagged.

        Returns:
            bool: True if the cell is flagged, False otherwise.
        """
        return self._is_flagged

    def is_revealed(self) -> bool:
        """
        Check if a cell is revealed.

        Returns:
            bool: True if the cell is revealed, False otherwise.
        """
        return self._is_revealed

    def __str__(self) -> str:
        """
        Get the string representation of the cell.

        Returns:
            str: String representation of the cell.
        """
        if self._is_revealed:
            if self._is_mine:
                return "*"
            if self._adjacent_mines:
                return str(self._adjacent_mines)
            return " "
        if self._is_flagged:
            return "F"
        return "#"
