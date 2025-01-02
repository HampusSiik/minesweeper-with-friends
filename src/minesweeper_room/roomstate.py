from typing import List

from minesweeper_room.player import Player
from minesweeper_room.gameoptions import GameOptions
from minesweeper.game.showboard import ShowBoard


class RoomState:

    _players: List[Player]
    """
    The players in the room.
    """

    _options: GameOptions
    """
    The options for the game.
    """

    _show_board: ShowBoard
    """
    The show board for the game.
    """

    _is_won: bool
    """
    Whether the game has been won.
    """

    _is_lost: bool
    """
    Whether the game has been lost.
    """

    def __init__(
        self,
        players: List[Player],
        options: GameOptions,
        show_board: ShowBoard,
        is_won: bool,
        is_lost: bool,
    ) -> None:
        """
        Initializes a new room with the given options.

        Args:
            players (List[Player]): The players in the room.
            options (GameOptions): The options for the game.
            show_board (ShowBoard): The show board for the game.
            is_won (bool): Whether the game has been won.
            is_lost (bool): Whether the game has been lost.
        """
        self._players = players
        self._options = options
        self._show_board = show_board
        self._is_won = is_won
        self._is_lost = is_lost

    def to_dict(self):
        return {
            "players": [player.to_dict() for player in self._players],
            "options": self._options.to_dict(),
            "show_board": self._show_board.to_dict(),
            "is_won": self._is_won,
            "is_lost": self._is_lost,
        }
