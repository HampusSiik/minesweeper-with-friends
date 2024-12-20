from minesweeper.cells.cell import Cell


class RevealedCell:

    _cell: Cell

    def __init__(self, cell: Cell):
        self._cell = cell

    def is_mine(self) -> bool:
        return self._cell.is_mine()

    def is_flagged(self) -> bool:
        return False

    def is_revealed(self) -> bool:
        return True

    def unwrap(self) -> Cell:
        return self._cell.unwrap()

    def flagged(self) -> Cell:
        return self._cell.flagged()

    def revealed(self) -> Cell:
        return self

    def __str__(self) -> str:
        return "R"
