import unittest
from minesweeper.board import board


class TestBoard(unittest.TestCase):

    _board: board.Board

    def setUp(self):
        self._board = board.Board()

    def test_generate_board(self):
        rows = 12
        cols = 10
        self._board.generate_board(rows, cols)
        for row in self._board._board:
            self.assertEqual(len(row), cols, "Columns not generated correctly")
            for cell in row:
                self.assertFalse(cell.is_mine(), "Mines generated in empty board")
        self.assertEqual(len(self._board._board), rows, "Rows not generated correctly")

    def test_place_mines(self):
        rows = 10
        cols = 10
        start_position = (0, 0)
        expected_mines = 10
        self._board.generate_board(rows, cols)
        self._board.place_mines(expected_mines, start_position)
        mines = 0
        if self._board._board[start_position[0]][start_position[1]].is_mine():
            self.fail("Start position is a mine")
        for row in self._board._board:
            for cell in row:
                if cell.is_mine():
                    mines += 1
        self.assertEqual(mines, expected_mines, "Mines placed incorrectly")

    def test_shape(self):
        rows = 12
        cols = 10
        self._board.generate_board(rows, cols)
        self.assertEqual(
            self._board.shape(), (rows, cols), "Shape not returned correctly"
        )

    def test_is_mine_empty(self):
        self._board.generate_board(10, 10)
        self._board.place_mines(10, (0, 0))
        self.assertFalse(
            self._board._board[0][0].is_mine(), "Mine not placed correctly"
        )

    def test_is_mine_mine(self):
        self._board.generate_board(10, 10)
        self._board.place_mines(99, (0, 0))
        self.assertTrue(self._board._board[0][1].is_mine(), "Mine not placed correctly")

    def test_is_flagged_empty(self):
        self._board.generate_board(10, 10)
        self.assertFalse(
            self._board._board[0][0].is_flagged(), "Flag not placed correctly"
        )

    def test_is_flagged_flagged(self):
        self._board.generate_board(10, 10)
        self._board._board[0][0].toggle_flag()
        self.assertTrue(
            self._board._board[0][0].is_flagged(), "Flag not placed correctly"
        )

    def test_is_revealed_empty(self):
        self._board.generate_board(10, 10)
        self.assertFalse(
            self._board._board[0][0].is_revealed(), "Cell not revealed correctly"
        )

    def test_is_revealed_revealed(self):
        self._board.generate_board(10, 10)
        self._board._board[0][0].reveal()
        self.assertTrue(
            self._board._board[0][0].is_revealed(), "Cell not revealed correctly"
        )

    def test_toggle_flag(self):
        self._board.generate_board(10, 10)
        self._board._board[0][0].toggle_flag()
        self.assertTrue(
            self._board._board[0][0].is_flagged(), "Flag not placed correctly"
        )
        self._board._board[0][0].toggle_flag()
        self.assertFalse(
            self._board._board[0][0].is_flagged(), "Flag not placed correctly"
        )

    def test_reveal(self):
        self._board.generate_board(10, 10)
        self._board._board[0][0].reveal()
        self.assertTrue(
            self._board._board[0][0].is_revealed(), "Cell not revealed correctly"
        )

    def test_all_positions(self):
        rows, cols = 10, 10
        cells = rows * cols
        self._board.generate_board(rows, cols)
        positions = self._board.all_positions()
        self.assertEqual(len(positions), cells, "All positions not returned correctly")
        for position in positions:
            self.assertTrue(
                0 <= position[0] < 10 and 0 <= position[1] < 10,
                "Position not in bounds",
            )
        self.assertEqual(
            len(set(positions)), cells, "Duplicate positions returned in all_positions"
        )

    def test_mined(self):
        self._board.generate_board(10, 10)
        self.assertFalse(self._board.mined(), "Mined returned incorrectly")
        self._board.place_mines(10, (0, 0))
        self.assertTrue(self._board.mined(), "Mined returned incorrectly")
