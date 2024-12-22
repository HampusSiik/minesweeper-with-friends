from minesweeper.cells.cell import Cell
from minesweeper.cells.flaggedcell import FlaggedCell
from minesweeper.cells.revealedcell import RevealedCell


class MineCell:

    def is_mine(self) -> bool:
        return True

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
        return "M"
