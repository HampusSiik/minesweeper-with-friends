from secrets import token_urlsafe

from .gameoptions import GameOptions
from .roomregistry import RoomRegistry
from .roomstate import RoomState
from .player import Player
from .gamestateupdater import GameStateUpdater


class RoomAPI:
    """
    Represents the API for managing rooms.
    """

    _room_registry: RoomRegistry
    """
    The registry of rooms.
    """

    _gamestate_updater: GameStateUpdater
    """
    The game state updater.
    """

    def __init__(self) -> None:
        """
        Initializes a new RoomAPI object.
        """
        self._gamestate_updater = GameStateUpdater()
        self._room_registry = RoomRegistry(self._gamestate_updater)

    def create_room(self, options: GameOptions) -> str:
        """
        Creates a new room with the given options.
        """
        room_id = self._generate_room_id()
        self._room_registry.new_room(options, room_id)
        return room_id

    def _generate_room_id(self) -> str:
        """
        Generates a new room ID.
        """
        room_id = token_urlsafe()
        while self._room_registry.id_exists(room_id):
            room_id = token_urlsafe()
        return room_id

    def join_room(self, room_id: str, player: Player) -> None:
        """
        Adds a player to the room.
        """
        self._room_registry.add_player(room_id, player)

    def leave_room(self, room_id: str, player: Player) -> None:
        """
        Removes a player from the room.
        """
        self._room_registry.remove_player(room_id, player)

    def update_room_options(self, room_id: str, options: GameOptions) -> None:
        """
        Updates the options of the room.
        """
        self._room_registry.update_options(room_id, options)

    def get_room_state(self, room_id: str) -> RoomState:
        return self._room_registry.get_room_state(room_id)
