import secrets
from typing import Callable, List

from .gameoptions import GameOptions
from .roomregistry import RoomRegistry
from .roomstate import RoomState
from .player import Player


class RoomAPI:
    """
    Represents the API for managing rooms.
    """

    _room_registry: RoomRegistry
    """
    The registry of rooms.
    """

    _update_observers: List[Callable[[RoomState], None]]
    """
    The list of observers to notify when a room is updated.
    """

    def __init__(self) -> None:
        """
        Initializes a new RoomAPI object.
        """
        self._room_registry = RoomRegistry()

    def _notify_observers(self, room_id: str) -> None:
        """
        Notifies all observers that a room has been updated.

        Args:
            room_id (str): The ID of the room.
        """
        room_state = self._room_registry.get_room_state(room_id)
        for observer in self._update_observers:
            observer(room_state)

    def add_update_observer(self, observer: Callable[[RoomState], None]) -> None:
        """
        Adds an observer to the list of observers.

        Args:
            observer (Callable[[RoomState], None]): The observer to add.
        """
        self._update_observers.append(observer)

    def create_room(self, options: GameOptions) -> str:
        """
        Creates a new room with the given options.

        Args:
            options (GameOptions): The options of the room.

        Returns:
            str: The ID of the new room.
        """
        room_id = self._generate_room_id()
        self._room_registry.new_room(options, room_id)
        return room_id

    def _generate_room_id(self) -> str:
        """
        Generates a new room ID.

        Returns:
            str: The new room ID.
        """
        room_id = secrets.token_urlsafe()
        while self._room_registry.id_exists(room_id):
            room_id = secrets.token_urlsafe()
        return room_id

    def join_room(self, room_id: str, player: Player) -> None:
        """
        Adds a player to the room.

        Args:
            room_id (str): The ID of the room.
            player (Player): The player to add.
        """
        self._room_registry.add_player(room_id, player)
        self._notify_observers(room_id)

    def leave_room(self, room_id: str, player: Player) -> None:
        """
        Removes a player from the room.

        Args:
            room_id (str): The ID of the room.
            player (Player): The player to remove.
        """
        self._room_registry.remove_player(room_id, player)
        self._notify_observers(room_id)

    def update_room_options(self, room_id: str, options: GameOptions) -> None:
        """
        Updates the options of the room.

        Args:
            room_id (str): The ID of the room.
            options (GameOptions): The new options of the room.
        """
        self._room_registry.update_options(room_id, options)
        self._notify_observers(room_id)

    def get_room_state(self, room_id: str) -> RoomState:
        """
        Gets the state of the room.

        Args:
            room_id (str): The ID of the room.

        Returns:
            RoomState: The state of the room.
        """
        return self._room_registry.get_room_state(room_id)
