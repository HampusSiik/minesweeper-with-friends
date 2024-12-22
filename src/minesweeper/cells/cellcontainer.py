from __future__ import annotations
from minesweeper.cells.cell import Cell
from minesweeper.cells.minecell import MineCell
from minesweeper.cells.emptycell import EmptyCell


class CellContainer:

    _cell: Cell

    def __init__(self, cell: Cell):
        self._cell = cell

    def is_mine(self) -> bool:
        return self._cell.is_mine()

    def is_flagged(self) -> bool:
        return self._cell.is_flagged()

    def is_revealed(self) -> bool:
        return self._cell.is_revealed()

    def unwraped(self) -> Cell:
        return self._cell.unwraped()

    def flag(self) -> None:
        self._cell = self._cell.flagged()

    def reveal(self) -> None:
        self._cell = self._cell.revealed()

    def __str__(self) -> str:
        return str(self._cell)

    @staticmethod
    def create_mine() -> CellContainer:
        return CellContainer(MineCell())

    @staticmethod
    def create_empty() -> CellContainer:
        return CellContainer(EmptyCell())
