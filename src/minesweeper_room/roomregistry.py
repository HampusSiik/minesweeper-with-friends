from typing import Dict, List, Callable

from .gameoptions import GameOptions
from .player import Player
from .room import Room
from .roomstate import RoomState


class RoomRegistry:
    """
    A class that handles the registration and retrieval of rooms.
    """

    _rooms: Dict[str, Room]
    """
    The rooms that are currently registered.
    """

    _update_observers: List[Callable[[str], None]]
    """
    The list of observers to notify when a room is updated.
    """

    def __init__(self):
        self._rooms = {}
        self._update_observers = []

    def add_update_observer(self, observer: Callable[[str], None]) -> None:
        """
        Adds an observer to the list of observers.

        Args:
            observer (Callable[[str], None]): The observer to add.
        """
        self._update_observers.append(observer)

    def _notify_observers(self, room_id: str) -> None:
        """
        Notifies all observers that a room has been updated.

        Args:
            room_id (str): The ID of the room.
        """
        for observer in self._update_observers:
            observer(room_id)

    def new_room(self, options: GameOptions, room_id: str) -> None:
        """
        Creates a new room with the given options.

        Args:
            options (GameOptions): The options for the room.
            room_id (str): The ID of the room.
        """
        room = Room(options)
        self._rooms[room_id] = room
        room.add_update_observer(lambda: self._notify_observers(room_id))

    def add_player(self, room_id: str, player: Player) -> None:
        """
        Adds a player to the room.

        Args:
            room_id (str): The ID of the room.
            player (Player): The player to add.
        """
        self._rooms[room_id].add_player(player)

    def remove_player(self, room_id: str, player: Player) -> None:
        """
        Removes a player from the room.

        Args:
            room_id (str): The ID of the room.
            player (Player): The player to remove.
        """
        self._rooms[room_id].remove_player(player)

    def update_options(self, room_id: str, options: GameOptions) -> None:
        """
        Updates the options for the room.

        Args:
            room_id (str): The ID of the room.
            options (GameOptions): The new options for the room.
        """
        self._rooms[room_id].update_options(options)

    def get_room_state(self, room_id: str) -> RoomState:
        """
        Returns the state of the room.

        Args:
            room_id (str): The ID of the room.

        Returns:
            RoomState: The state of the room.
        """
        room = self._rooms[room_id]
        return RoomState(
            room.get_players(),
            room.get_game_options(),
            room.get_show_board(),
            room.is_won(),
            room.is_lost(),
        )

    def id_exists(self, room_id: str) -> bool:
        """
        Checks if a room with the given ID exists.

        Args:
            room_id (str): The ID of the room.

        Returns:
            bool: True if the room exists, False otherwise.
        """
        return room_id in self._rooms
