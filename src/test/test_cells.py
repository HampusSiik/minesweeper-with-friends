import unittest
from typing import Any
from abc import ABC, abstractmethod

from minesweeper.cells import (
    cell,
    emptycell,
    minecell,
    cellcontainer,
    revealedcell,
    flaggedcell,
)


class TestCell(ABC):

    cell: cell.Cell

    @abstractmethod
    def setUp(self): ...

    @abstractmethod
    def assertTrue(self, expr: Any, msg: Any = None): ...

    def test_is_mine_returns_bool(self):
        self.assertTrue(isinstance(self.cell.is_mine(), bool))

    def test_is_flagged_returns_bool(self):
        self.assertTrue(isinstance(self.cell.is_flagged(), bool))

    def test_is_revealed_returns_bool(self):
        self.assertTrue(isinstance(self.cell.is_revealed(), bool))

    def test_flagged_returns_flagged_cell(self):
        self.assertTrue(isinstance(self.cell.flagged(), flaggedcell.FlaggedCell))

    def test_revealed_returns_revealed_cell(self):
        self.assertTrue(isinstance(self.cell.revealed(), revealedcell.RevealedCell))

    def test_flagged(self):
        self.assertTrue(self.cell.flagged().is_flagged())

    def test_revealed(self):
        self.assertTrue(self.cell.revealed().is_revealed())


class TestEmptyCell(unittest.TestCase, TestCell):

    def setUp(self):
        self.cell = emptycell.EmptyCell()

    def test_is_mine(self):
        self.assertFalse(self.cell.is_mine())

    def test_is_flagged(self):
        self.assertFalse(self.cell.is_flagged())

    def test_is_revealed(self):
        self.assertFalse(self.cell.is_revealed())

    def test_unwraped(self):
        self.assertTrue(self.cell is self.cell.unwraped())


class TestMineCell(unittest.TestCase, TestCell):

    def setUp(self):
        self.cell = minecell.MineCell()

    def test_is_mine(self):
        self.assertTrue(self.cell.is_mine())

    def test_is_flagged(self):
        self.assertFalse(self.cell.is_flagged())

    def test_is_revealed(self):
        self.assertFalse(self.cell.is_revealed())

    def test_unwraped(self):
        self.assertTrue(self.cell is self.cell.unwraped())


class TestFlaggedCellEmpty(unittest.TestCase, TestCell):

    def setUp(self):
        self.cell = flaggedcell.FlaggedCell(emptycell.EmptyCell())

    def test_is_mine(self):
        self.assertTrue(self.cell.is_mine() == self.cell.unwraped().is_mine())

    def test_is_flagged(self):
        self.assertTrue(self.cell.is_flagged())

    def test_is_revealed(self):
        self.assertFalse(self.cell.is_revealed())

    def test_unwrap(self):
        self.assertTrue(self.cell is not self.cell.unwraped())


class TestFlaggedCellMine(unittest.TestCase, TestCell):

    def setUp(self):
        self.cell = flaggedcell.FlaggedCell(minecell.MineCell())


class TestRevealedCellEmpty(TestFlaggedCellEmpty):

    def setUp(self):
        self.cell = revealedcell.RevealedCell(emptycell.EmptyCell())

    def test_is_flagged(self):
        self.assertFalse(self.cell.is_flagged())

    def test_is_revealed(self):
        self.assertTrue(self.cell.is_revealed())


class TestRevealedCellMine(TestRevealedCellEmpty):

    def setUp(self):
        self.cell = revealedcell.RevealedCell(minecell.MineCell())


class TestCellContainer(unittest.TestCase):

    cell_container: cellcontainer.CellContainer

    def setUp(self):
        self.cell_container = cellcontainer.CellContainer.create_empty()

    def test_is_mine(self):
        self.assertFalse(self.cell_container.is_mine())

    def test_unwraped(self):
        self.assertTrue(isinstance(self.cell_container.unwraped(), cell.Cell))

    def test_flag(self):
        self.cell_container.flag()
        self.assertTrue(self.cell_container.is_flagged())

    def test_reveal(self):
        self.cell_container.reveal()
        self.assertTrue(self.cell_container.is_revealed())


class TestCellContainerCreateMine(TestCellContainer):

    def setUp(self):
        self.cell_container = cellcontainer.CellContainer.create_mine()

    def test_is_mine(self):
        self.assertTrue(self.cell_container.is_mine())
