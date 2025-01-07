from typing import List, Callable

from minesweeper.position import Position
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

    _update_observers: List[Callable[[], None]]
    """
    The list of observers to notify when the room is updated.
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
        self.start_game()
        self._update_observers = []

    def add_update_observer(self, observer: Callable[[], None]) -> None:
        """
        Adds an observer to the list of observers.

        Args:
            observer (Callable[[], None]): The observer to add.
        """
        self._update_observers.append(observer)

    def _notify_observers(self) -> None:
        """
        Notifies all observers that the room has been updated.
        """
        for observer in self._update_observers:
            observer()

    def add_player(self, player: Player) -> None:
        """
        Adds a player to the room.

        Args:
            player (Player): The player to add.
        """
        player.set_leave_callback(self.remove_player)
        player.set_left_click_callback(self._left_click)
        player.set_right_click_callback(self._right_click)
        self._players.append(player)
        self._notify_observers()

    def _left_click(self, player: Player, position: Position) -> None:
        """
        Handle a left click on the board.

        Args:
            player (Player): The player who clicked.
            position (Position): The position clicked.
        """
        self._game.left_click_cell(position)
        self._notify_observers()

    def _right_click(self, player: Player, position: Position) -> None:
        """
        Handle a right click on the board.

        Args:
            player (Player): The player who clicked.
            position (Position): The position clicked.
        """
        self._game.right_click_cell(position)
        self._notify_observers()

    def remove_player(self, player: Player) -> None:
        """
        Removes a player from the room.

        Args:
            player (Player): The player to remove.
        """
        player.reset_callbacks()
        self._players.remove(player)
        self._notify_observers()

    def update_options(self, options: GameOptions) -> None:
        """
        Updates the options for the game.

        Args:
            options (GameOptions): The new options for the game.
        """
        self._options = options
        self.start_game()
        self._notify_observers()

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

    def get_game_options(self) -> GameOptions:
        """
        Get the game options.

        Returns:
            GameOptions: The game options.
        """
        return self._options

    def get_players(self) -> List[Player]:
        """
        Get the players in the room.

        Returns:
            List[Player]: The players in the room.
        """
        return self._players
