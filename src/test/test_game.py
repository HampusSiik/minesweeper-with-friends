import unittest
from minesweeper.game.minesweeper import Minesweeper


class TestMinesweeper(unittest.TestCase):

    def test_shape(self):
        m = Minesweeper()
        self.assertEqual(m.shape(), (1, 0))

    def test_game_lost_false(self):
        m = Minesweeper()
        self.assertFalse(m.game_lost())

    def test_game_won_false(self):
        m = Minesweeper()
        m.generate_board(1, 1)
        self.assertFalse(m.game_won())

    def test_left_click_cell(self):
        m = Minesweeper()
        m.generate_board(1, 1)
        m.left_click_cell((0, 0))
        self.assertTrue(m.game_won())

    def test_right_click_cell(self):
        m = Minesweeper()
        m.generate_board(1, 1)
        m.right_click_cell((0, 0))
        self.assertTrue(m._board.is_flagged((0, 0)))

    def test_game_lost_true(self):
        m = Minesweeper()
        m.generate_board(1, 2)
        m._board.place_mines(1, (0, 1))
        m.left_click_cell((0, 0))
        self.assertTrue(m.game_lost())
