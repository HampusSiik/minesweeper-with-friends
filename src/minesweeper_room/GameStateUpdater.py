from typing import List, Callable, Dict

from minesweeper_room.roomstate import RoomState


RoomUpdateListener = Callable[[RoomState], None]
AnyUpdateListener = Callable[[str, RoomState], None]


class GameStateUpdater:
    """
    A class that handles updating the game state and notifying listeners.
    """

    _room_update_listeners: Dict[str, List[RoomUpdateListener]]
    """
    The listeners for room state updates.
    """

    _any_update_listeners: List[AnyUpdateListener]
    """
    The listeners for any state updates.
    """

    def __init__(self):
        self._room_update_listeners = {}
        self._any_update_listeners = []

    def notify_state_update(self, room_id: str, state: RoomState):
        """
        Notifies the room that the state has updated.

        Args:
            room_id (str): The room to notify.
            state (RoomState): The new state of the room.
        """
        self._notify_room_state_update(room_id, state)
        self._notify_any_state_update(room_id, state)

    def _notify_room_state_update(self, room_id: str, state: RoomState):
        """
        Notifies the room that the state has updated.

        Args:
            room_id (str): The room to notify.
            state (RoomState): The new state of the room.
        """
        for listener in self._room_update_listeners.get(room_id, []):
            listener(state)

    def _notify_any_state_update(self, room_id: str, state: RoomState):
        """
        Notifies the room that the state has updated.

        Args:
            room_id (str): The room to notify.
            state (RoomState): The new state of the room.
        """
        for listener in self._any_update_listeners:
            listener(room_id, state)

    def add_room_update_listener(self, room_id: str, listener: RoomUpdateListener):
        """
        Adds a listener for room state updates.

        Args:
            room_id (str): The room to add the listener to.
            listener (RoomUpdateListener): The listener to add.
        """
        self._room_update_listeners.setdefault(room_id, []).append(listener)

    def add_any_update_listener(self, listener: AnyUpdateListener):
        """
        Adds a listener for any state updates.

        Args:
            listener (AnyUpdateListener): The listener to add.
        """
        self._any_update_listeners.append(listener)
