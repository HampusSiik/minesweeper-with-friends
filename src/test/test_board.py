import unittest
from minesweeper.board import Board


class TestBoard(unittest.TestCase):

    board: Board

    def setUp(self):
        self.board = Board()

    def test_generate_board(self):
        rows = 12
        cols = 10
        self.board.generate_board(rows, cols)
        for row in self.board._board:
            self.assertEqual(len(row), cols, "Columns not generated correctly")
            for cell in row:
                self.assertFalse(cell.is_mine(), "Mines generated in empty board")
        self.assertEqual(len(self.board._board), rows, "Rows not generated correctly")

    def test_place_mines(self):
        rows = 10
        cols = 10
        start_position = (0, 0)
        expected_mines = 10
        self.board.generate_board(rows, cols)
        self.board.place_mines(expected_mines, start_position)
        mines = 0
        if self.board._board[start_position[0]][start_position[1]].is_mine():
            self.fail("Start position is a mine")
        for row in self.board._board:
            for cell in row:
                if cell.is_mine():
                    mines += 1
        self.assertEqual(mines, expected_mines, "Mines placed incorrectly")
