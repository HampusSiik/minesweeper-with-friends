from typing import Dict

from minesweeper_room.gameoptions import GameOptions
from minesweeper_room.player import Player
from minesweeper_room.gamestateupdater import GameStateUpdater
from minesweeper_room.room import Room
from minesweeper_room.roomstate import RoomState


class RoomRegistry:
    """
    A class that handles the registration and retrieval of rooms.
    """

    _rooms: Dict[str, Room]
    """
    The rooms that are currently registered.
    """

    _updater: GameStateUpdater
    """
    The updater to notify when rooms are updated.
    """

    def __init__(self, updater: GameStateUpdater):
        self._rooms = {}
        self._updater = updater

    def new_room(self, options: GameOptions, room_id: str) -> None:
        """
        Creates a new room with the given options.

        Args:
            options (GameOptions): The options for the room.
            room_id (str): The ID of the room.
        """
        self._rooms[room_id] = Room(options)

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
        self._updater.notify_state_update(room_id, self.get_room_state(room_id))

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
