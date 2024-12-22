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
