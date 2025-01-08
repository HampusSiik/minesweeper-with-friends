from __future__ import annotations
from typing import Protocol, runtime_checkable


@runtime_checkable
class Cell(Protocol):
    """
    A cell in the minesweeper game.
    """

    def is_mine(self) -> bool:
        """
        Returns True if the cell is a mine, False otherwise.

        Returns:
            bool: True if the cell is a mine, False otherwise.
        """
        ...

    def is_flagged(self) -> bool:
        """
        Returns True if the cell is flagged, False otherwise.

        Returns:
            bool: True if the cell is flagged, False otherwise.
        """
        ...

    def is_revealed(self) -> bool:
        """
        Returns True if the cell is revealed, False otherwise.

        Returns:
            bool: True if the cell is revealed, False otherwise.
        """
        ...

    def unwraped(self) -> Cell:
        """
        Returns the unwrapped cell.

        Returns:
            Cell: The unwrapped cell.
        """
        ...

    def flagged(self) -> Cell:
        """
        Returns a flagged cell.

        Returns:
            Cell: A flagged cell.
        """
        ...

    def revealed(self) -> Cell:
        """
        Returns a revealed cell.

        Returns:
            Cell: A revealed cell.
        """
        ...

    def __str__(self) -> str:
        """
        Returns a string representation of the cell.

        Returns:
            str: A string representation of the cell.
        """
        ...
