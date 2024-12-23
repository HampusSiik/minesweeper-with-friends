import unittest

from minesweeper.game.showboard import ShowBoard
from minesweeper.board.board import Board


class TestShowBoard(unittest.TestCase):

    b: Board

    def setUp(self):
        self.b = Board()
        self.b.generate_board(5, 10)
        self.b.place_mines(5, (0, 0))

    def test_showboard(self):
        sb = ShowBoard(self.b)
