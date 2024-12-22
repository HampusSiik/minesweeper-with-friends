"""Empty cell class"""

from minesweeper.cells.cell import Cell
from minesweeper.cells.flaggedcell import FlaggedCell
from minesweeper.cells.revealedcell import RevealedCell


class EmptyCell:

    def is_mine(self) -> bool:
        return False

    def is_flagged(self) -> bool:
        return False

    def is_revealed(self) -> bool:
        return False

    def unwraped(self) -> Cell:
        return self

    def flagged(self) -> Cell:
        return FlaggedCell(self)

    def revealed(self) -> Cell:
        return RevealedCell(self)

    def __str__(self) -> str:
        return "E"
