import unittest
from minesweeper_room.player import Player
from minesweeper_room.gameoptions import GameOptions
from minesweeper.game.showboard import ShowBoard
from minesweeper_api.roomstate import RoomState
from minesweeper.game.minesweeper import Minesweeper


class TestRoomState(unittest.TestCase):

    def setUp(self):
        self.minesweeper = Minesweeper()
        self.players = [Player("player1"), Player("player2")]
        self.options = GameOptions(10, 10, 10)
        self.minesweeper.generate_game(
            self.options.rows(), self.options.cols(), self.options.mines()
        )
        self.show_board = self.minesweeper.get_show_board()
        self.is_won = False
        self.is_lost = False
        self.room_state = RoomState(
            self.players, self.options, self.show_board, self.is_won, self.is_lost
        )

    def test_initialization(self):
        self.assertEqual(
            self.room_state._players, self.players, "Players not initialized correctly"
        )
        self.assertEqual(
            self.room_state._options, self.options, "Options not initialized correctly"
        )
        self.assertEqual(
            self.room_state._show_board,
            self.show_board,
            "ShowBoard not initialized correctly",
        )
        self.assertEqual(
            self.room_state._is_won, self.is_won, "is_won not initialized correctly"
        )
        self.assertEqual(
            self.room_state._is_lost, self.is_lost, "is_lost not initialized correctly"
        )

    def test_to_dict(self):
        room_state_dict = self.room_state.to_dict()
        self.assertEqual(
            room_state_dict["players"],
            [player.to_dict() for player in self.players],
            "Players not converted to dict correctly",
        )
        self.assertEqual(
            room_state_dict["options"],
            self.options.to_dict(),
            "Options not converted to dict correctly",
        )
        self.assertEqual(
            room_state_dict["show_board"],
            self.show_board.to_dict(),
            "ShowBoard not converted to dict correctly",
        )
        self.assertEqual(
            room_state_dict["is_won"],
            self.is_won,
            "is_won not converted to dict correctly",
        )
        self.assertEqual(
            room_state_dict["is_lost"],
            self.is_lost,
            "is_lost not converted to dict correctly",
        )


if __name__ == "__main__":
    unittest.main()
