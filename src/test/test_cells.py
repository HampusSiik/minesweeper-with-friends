import unittest

from minesweeper.cells import (
    emptycell,
    minecell,
    cellcontainer,
    cell,
    revealedcell,
    flaggedcell,
)


class TestEmptyCell(unittest.TestCase):

    def test_create(self):
        try:
            emptycell.EmptyCell()
            self.assertTrue(True)
        except Exception:
            self.fail("Could not create EmptyCell")

    def test_is_mine(self):
        ec = emptycell.EmptyCell()
        self.assertFalse(ec.is_mine())

    def test_is_flagged(self):
        ec = emptycell.EmptyCell()
        self.assertFalse(ec.is_flagged())

    def test_is_revealed(self):
        ec = emptycell.EmptyCell()
        self.assertFalse(ec.is_revealed())

    def test_flagged(self):
        ec = emptycell.EmptyCell()
        self.assertTrue(ec.flagged().is_flagged())

    def test_unwrap(self):
        ec = emptycell.EmptyCell()
        self.assertTrue(ec is ec.unwrap())
