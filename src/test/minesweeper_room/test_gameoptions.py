import unittest

from itertools import permutations

from minesweeper_room.gameoptions import GameOptions


def _test_to_dict(testcase: unittest.TestCase, mines: int, cols: int, rows: int):
    game_options = GameOptions(mines, cols, rows)
    testcase.assertEqual(
        game_options.to_dict(), {"mines": mines, "cols": cols, "rows": rows}
    )


class TestGameOptions(unittest.TestCase):
    def test_mines(self):
        game_options = GameOptions(10, 10, 10)
        self.assertEqual(game_options.mines(), 10)

    def test_cols(self):
        game_options = GameOptions(10, 10, 10)
        self.assertEqual(game_options.cols(), 10)

    def test_rows(self):
        game_options = GameOptions(10, 10, 10)
        self.assertEqual(game_options.rows(), 10)

    def test_to_dict(self):
        for mines, cols, rows in permutations(range(10, 40), 3):
            _test_to_dict(self, mines, cols, rows)
