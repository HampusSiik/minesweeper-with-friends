from __future__ import annotations
from typing import Callable, Dict

from minesweeper.position import Position


class Player:
    """
    Represents a player in the game.
    """

    _name: str
    """
    The name of the player.
    """

    _leave_callback: Callable[[Player], None]
    """
    The callback function to call when the player leaves the room.
    """

    _right_click_callback: Callable[[Player, Position], None]
    """
    The callback function to call when the player right-clicks on a cell.
    """

    _left_click_callback: Callable[[Player, Position], None]
    """
    The callback function to call when the player left-clicks on a cell.
    """

    _reset_callback: Callable[[Player], None]
    """
    The callback function to call when the player resets the game.
    """

    @staticmethod
    def from_dict(data: Dict[str, str]) -> Player:
        """
        Converts a dictionary to a Player object.

        Args:
            data (dict): The dictionary to convert.

        Returns:
            Player: The Player object.
        """
        return Player(data["name"])

    @staticmethod
    def standard_callback(*_) -> None:
        """
        A standard callback function that does nothing.

        Args:
            _: Any arguments passed to the callback.
        """
        pass

    def __init__(self, name: str):
        """
        Initializes a new Player object.
        """
        self._name = name
        self._leave_callback = self._right_click_callback = (
            self._left_click_callback
        ) = self._reset_callback = Player.standard_callback

    def name(self) -> str:
        """
        Returns the name of the player.

        Returns:
            str: The name of the player.
        """
        return self._name

    def leave_room(self) -> None:
        """
        Leaves the room and calls the leave callback function.
        """
        self._leave_callback(self)

    def right_click(self, position: Position) -> None:
        """
        Handles a right-click action on a cell.
        """
        self._right_click_callback(self, position)

    def left_click(self, position: Position) -> None:
        """
        Handles a left-click action on a cell.
        """
        self._left_click_callback(self, position)

    def reset_game(self) -> None:
        """
        Resets the game and calls the reset callback function.
        """
        self._reset_callback(self)

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the Player object to a dictionary.

        Returns:
            dict: The dictionary representation of the Player object.
        """
        return {
            "name": self._name,
        }

    def set_leave_callback(self, callback: Callable[[Player], None]) -> None:
        """
        Sets the callback function to call when the player leaves the room.

        Args:
            callback (Callable[[Player], None]): The callback function.
        """
        self._leave_callback = callback

    def set_right_click_callback(
        self, callback: Callable[[Player, Position], None]
    ) -> None:
        """
        Sets the callback function to call when the player right-clicks on a
        cell.

        Args:
            callback (Callable[[Player, Position], None]): The callback.
        """
        self._right_click_callback = callback

    def set_left_click_callback(
        self, callback: Callable[[Player, Position], None]
    ) -> None:
        """
        Sets the callback function to call when the player left-clicks on a
        cell.

        Args:
            callback (Callable[[Player, Position], None]): The callback.
        """
        self._left_click_callback = callback

    def reset_callbacks(self) -> None:
        """
        Resets the callbacks to the standard callback function.
        """
        self._leave_callback = self._right_click_callback = (
            self._left_click_callback
        ) = Player.standard_callback

    def set_reset_callback(self, callback: Callable[[Player], None]) -> None:
        """
        Sets the callback function to call when the player resets the game.

        Args:
            callback (Callable[[Player], None]): The callback function.
        """
        self._reset_callback = callback
