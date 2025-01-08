import unittest
from minesweeper.game.minesweeper import Minesweeper


class TestMinesweeper(unittest.TestCase):

    def test_shape_no_board(self):
        m = Minesweeper()
        self.assertEqual(m.shape(), (1, 0))

    def test_shape(self):
        rows, cols = 10, 15
        m = Minesweeper()
        m.generate_game(rows, cols, 0)
        self.assertEqual(m.shape(), (rows, cols))

    def test_game_lost_false(self):
        m = Minesweeper()
        self.assertFalse(m.is_lost())

    def test_game_won_false(self):
        m = Minesweeper()
        m.generate_game(1, 1, 0)
        self.assertFalse(m.is_won())

    def test_left_click_cell(self):
        m = Minesweeper()
        m.generate_game(1, 1, 0)
        m.left_click_cell((0, 0))
        self.assertTrue(m.is_won())

    def test_right_click_cell(self):
        m = Minesweeper()
        m.generate_game(1, 1, 0)
        m.right_click_cell((0, 0))
        self.assertTrue(m._board.is_flagged((0, 0)))

    def test_game_lost_true(self):
        m = Minesweeper()
        m.generate_game(1, 3, 1)
        m.left_click_cell((0, 0))
        m.left_click_cell((0, 2))
        self.assertTrue(m.is_lost())

    def test_generate_game(self):
        m = Minesweeper()
        m.generate_game(10, 10, 10)
        m.left_click_cell((0, 0))
        self.assertEqual(m._board.mines(), 10)
        self.assertEqual(m._board.shape(), (10, 10))
        self.assertFalse(m.is_lost())
        self.assertEqual(m._mines, 10)
        self.assertEqual(m._board.mines(), 10)
        self.assertEqual(m._board.shape(), (10, 10))

    def test_generate_game_no_mines(self):
        m = Minesweeper()
        m.generate_game(10, 10, 0)
        m.left_click_cell((0, 0))
        self.assertEqual(m._board.mines(), 0)
        self.assertEqual(m._board.shape(), (10, 10))
        self.assertFalse(m.is_lost())
        self.assertEqual(m._mines, 0)
        self.assertEqual(m._board.mines(), 0)
        self.assertEqual(m._board.shape(), (10, 10))

    def test_right_click_cell_revealed(self):
        m = Minesweeper()
        m.generate_game(1, 1, 0)
        m.left_click_cell((0, 0))
        m.right_click_cell((0, 0))
        self.assertFalse(m._board.is_flagged((0, 0)))

    def test_right_click_cell_flagged(self):
        m = Minesweeper()
        m.generate_game(1, 1, 0)
        m.right_click_cell((0, 0))
        self.assertTrue(m._board.is_flagged((0, 0)))
        m.right_click_cell((0, 0))
        self.assertFalse(m._board.is_flagged((0, 0)))

    def test_mines_generated(self):
        m = Minesweeper()
        m.generate_game(10, 10, 10)
        m.left_click_cell((0, 0))
        self.assertTrue(m.mines_generated())

    def test_mines_not_generated(self):
        m = Minesweeper()
        m.generate_game(10, 10, 10)
        self.assertFalse(m.mines_generated())

    def test_right_click_cell_no_mines_generated(self):
        m = Minesweeper()
        m.generate_game(10, 10, 10)
        m.right_click_cell((0, 0))
        self.assertFalse(m._board.is_flagged((0, 0)))

    def test_left_click_cell_no_mines_generated(self):
        m = Minesweeper()
        m.generate_game(10, 10, 10)
        m.left_click_cell((0, 0))
        self.assertTrue(m.mines_generated())
