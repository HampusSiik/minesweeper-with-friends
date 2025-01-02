import unittest
from minesweeper_room.player import Player
from minesweeper.position import Position


class TestPlayer(unittest.TestCase):

    _player: Player

    _player_name: str = "TestPlayer"

    def setUp(self):
        self._player = Player(self._player_name)

    def test_name(self):
        self.assertEqual(
            self._player.name(), self._player_name, "Name not returned correctly"
        )

    def test_leave_room(self):
        executed = False

        def callback(player):
            nonlocal executed
            executed = True
            self.assertEqual(
                player, self._player, "Player not passed correctly to callback"
            )

        self._player.set_leave_callback(callback)
        self._player.leave_room()
        self.assertTrue(executed, "Callback not executed")

    def test_right_click(self):
        expected_position = (0, 0)
        executed = False

        def callback(player, position):
            nonlocal executed
            executed = True
            self.assertEqual(
                player, self._player, "Player not passed correctly to callback"
            )
            self.assertEqual(
                position, expected_position, "Position not passed correctly to callback"
            )

        self._player.set_right_click_callback(callback)
        self._player.right_click(expected_position)
        self.assertTrue(executed, "Callback not executed")

    def test_left_click(self):
        expected_position = (0, 0)
        executed = False

        def callback(player, position):
            nonlocal executed
            executed = True

            self.assertEqual(
                player, self._player, "Player not passed correctly to callback"
            )
            self.assertEqual(
                position, expected_position, "Position not passed correctly to callback"
            )

        self._player.set_right_click_callback(callback)
        self._player.right_click(expected_position)
        self.assertTrue(executed, "Callback not executed")

    def test_to_dict(self):
        self.assertEqual(
            self._player.to_dict(),
            {"name": "TestPlayer"},
            "Dict not returned correctly",
        )

    def test_from_dict(self):
        player = Player.from_dict({"name": self._player_name})
        self.assertEqual(
            player.name(), self._player_name, "Player not created correctly"
        )
