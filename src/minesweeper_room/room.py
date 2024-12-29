from typing import List, Optional

from minesweeper.game.minesweeper import Minesweeper
from minesweeper.game.showboard import ShowBoard

from .player import Player
from .gameoptions import GameOptions


class Room:
    """
    Represents a room in which a game of Minesweeper is played.
    """

    _players: List[Player]
    """
    The players in the room.
    """

    _game: Minesweeper
    """
    The game being played in the room.
    """

    _options: GameOptions
    """
    The options for the game.
    """

    def __init__(self, options: GameOptions) -> None:
        """
        Initializes a new room with the given options.

        Args:
            options (GameOptions): The options for the game.
            room_id (str): The ID of the room.
        """
        self._players = []
        self._game = Minesweeper()
        self._options = options

    def add_player(self, player: Player) -> None:
        """
        Adds a player to the room.

        Args:
            player (Player): The player to add.
        """
        self._players.append(player)

    def remove_player(self, player: Player) -> None:
        """
        Removes a player from the room.

        Args:
            player (Player): The player to remove.
        """
        self._players.remove(player)

    def update_options(self, options: GameOptions) -> None:
        """
        Updates the options for the game.

        Args:
            options (GameOptions): The new options for the game.
        """
        self._options = options

    def start_game(self) -> None:
        """
        Starts a new game in the room.
        """
        self._game = Minesweeper()
        self._game.generate_game(
            self._options.rows(),
            self._options.cols(),
            self._options.mines(),
        )

    def is_won(self) -> bool:
        """
        Check if the game is won.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        return self._game.is_won()

    def is_lost(self) -> bool:
        """
        Check if the game is lost.

        Returns:
            bool: True if the game is lost, False otherwise.
        """
        return self._game.is_lost()

    def get_show_board(self) -> ShowBoard:
        """
        Get the board to show to the players.

        Returns:
            ShowBoard: The board to show to the players.
        """
        return self._game.get_show_board()
