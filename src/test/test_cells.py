import unittest

from minesweeper.cells import emptycell


class TestEmptyCell(unittest.TestCase):

    def test_create(self):
        try:
            emptycell.EmptyCell()
            self.assertTrue(True)
        except Exception:
            self.fail("Could not create EmptyCell")
