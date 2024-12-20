from minesweeper.cells.cell import Cell


class FlaggedCell:

    _cell: Cell

    def __init__(self, cell: Cell):
        self._cell = cell

    def is_mine(self) -> bool:
        return self._cell.is_mine()

    def is_flagged(self) -> bool:
        return True

    def is_revealed(self) -> bool:
        return False

    def unwrap(self) -> Cell:
        return self._cell.unwrap()

    def flagged(self) -> Cell:
        return self

    def revealed(self) -> Cell:
        return self._cell.revealed()

    def __str__(self) -> str:
        return "F"
