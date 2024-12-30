import unittest

from minesweeper_room.room import Room
from minesweeper_room.gameoptions import GameOptions
from minesweeper_room.player import Player
from minesweeper.game.showboard import ShowBoard


class TestRoom(unittest.TestCase):

    _room: Room

    _game_options: GameOptions

    _test_player: Player

    def setUp(self):
        self._test_player = Player("test_player")
        self._game_options = GameOptions(10, 10, 10)
        self._room = Room(self._game_options)

    def test_add_player(self):
        self._room.add_player(self._test_player)
        self.assertEqual(
            self._room._players, [self._test_player], "Player not added correctly"
        )

    def test_remove_player(self):
        self._room.add_player(self._test_player)
        self._room.remove_player(self._test_player)
        self.assertEqual(self._room._players, [], "Player not removed correctly")

    def test_update_options(self):
        new_options = GameOptions(20, 20, 20)
        self._room.update_options(new_options)
        self.assertEqual(
            self._room._options, new_options, "Options not updated correctly"
        )

    def test_start_game(self):
        self._room.start_game()
        self.assertTrue(self._room._game.get_show_board(), "Game not started correctly")

    def test_is_won(self):
        self._room.start_game()
        self.assertFalse(self._room.is_won(), "Game should not be won yet")

    def test_is_lost(self):
        self._room.start_game()
        self.assertFalse(self._room.is_lost(), "Game should not be lost yet")

    def test_show_board_not_None(self):
        self._room.start_game()
        show_board = self._room.get_show_board()
        self.assertIsNotNone(show_board, "ShowBoard not returned correctly")

    def test_show_board_is_ShowBoard(self):
        self._room.start_game()
        show_board = self._room.get_show_board()
        self.assertIsInstance(show_board, ShowBoard, "ShowBoard not returned correctly")

    def test_get_game_options(self):
        self.assertEqual(
            self._room.get_game_options(),
            self._game_options,
            "Game options not returned correctly",
        )
