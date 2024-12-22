import unittest
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

    def test_is_mine_returns_bool(self):
        self.assertTrue(isinstance(self.cell.is_mine(), bool))

    def test_is_flagged_returns_bool(self):
        self.assertTrue(isinstance(self.cell.is_flagged(), bool))

    def test_is_revealed_returns_bool(self):
        self.assertTrue(isinstance(self.cell.is_revealed(), bool))

    def test_flagged_returns_flagged_cell(self):
        self.assertTrue(isinstance(self.cell.flagged(), flaggedcell.FlaggedCell))


class TestEmptyCell(unittest.TestCase, TestCell):

    def setUp(self):
        self.cell = emptycell.EmptyCell()

    def test_is_mine(self):
        self.assertFalse(self.cell.is_mine())

    def test_is_flagged(self):
        self.assertFalse(self.cell.is_flagged())

    def test_is_revealed(self):
        self.assertFalse(self.cell.is_revealed())

    def test_flagged(self):
        self.assertTrue(self.cell.flagged().is_flagged())

    def test_unwrap(self):
        self.assertTrue(self.cell is self.cell.unwrap())


class TestMineCell(unittest.TestCase, TestCell):

    def setUp(self):
        self.cell = minecell.MineCell()

    def test_is_mine(self):
        self.assertTrue(self.cell.is_mine())

    def test_is_flagged(self):
        self.assertFalse(self.cell.is_flagged())

    def test_is_revealed(self):
        self.assertFalse(self.cell.is_revealed())

    def test_flagged(self):
        self.assertTrue(self.cell.flagged().is_flagged())

    def test_unwrap(self):
        self.assertTrue(self.cell is self.cell.unwrap())
