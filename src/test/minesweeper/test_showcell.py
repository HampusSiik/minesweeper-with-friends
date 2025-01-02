import unittest

from minesweeper.game.showcell import ShowCell


class TestShowCell(unittest.TestCase):

    def test_showcell(self):
        sc = ShowCell(None, None, False, False)
        self.assertIsNone(sc.adjacent_mines())
        self.assertIsNone(sc.is_mine())
        self.assertFalse(sc._is_flagged)
        self.assertFalse(sc._is_revealed)

    def test_adjacent_mines(self):
        sc = ShowCell(5, None, False, True)
        self.assertEqual(sc.adjacent_mines(), 5)

    def test_is_mine(self):
        sc = ShowCell(None, True, False, True)
        self.assertTrue(sc.is_mine())

    def test_is_flagged(self):
        sc = ShowCell(0, False, True, True)
        self.assertTrue(sc._is_flagged)

    def test_is_revealed(self):
        sc = ShowCell(0, False, False, True)
        self.assertTrue(sc._is_revealed)

    def test_str(self):
        sc = ShowCell(5, False, False, True)
        self.assertEqual(str(sc), "5")
        sc = ShowCell(None, True, False, True)
        self.assertEqual(str(sc), "*")
        sc = ShowCell(None, None, False, False)
        self.assertEqual(str(sc), "#")
        sc = ShowCell(None, None, True, False)
        self.assertEqual(str(sc), "F")
        sc = ShowCell(None, None, False, True)
        self.assertEqual(str(sc), " ")
        sc = ShowCell(0, None, False, True)
        self.assertEqual(str(sc), " ")
