from __future__ import annotations
from typing import Callable, Dict

from minesweeper.position import Position


class Player:

    _name: str
    _leave_callback: Callable[[Player], None]
    _right_click_callback: Callable[[Player, Position], None]
    _left_click_callback: Callable[[Player, Position], None]

    @staticmethod
    def from_dict(data: Dict[str, str]) -> Player:
        return Player(data["name"])

    @staticmethod
    def standard_callback(*_) -> None:
        pass

    def __init__(self, name: str):
        self._name = name
        self._leave_callback = self._right_click_callback = (
            self._left_click_callback
        ) = Player.standard_callback

    def name(self) -> str:
        return self._name

    def leave_room(self) -> None:
        self._leave_callback(self)

    def right_click(self, position: Position) -> None:
        self._right_click_callback(self, position)

    def left_click(self, position: Position) -> None:
        self._left_click_callback(self, position)

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self._name,
        }

    def set_leave_callback(self, callback: Callable[[Player], None]) -> None:
        self._leave_callback = callback

    def set_right_click_callback(
        self, callback: Callable[[Player, Position], None]
    ) -> None:
        self._right_click_callback = callback

    def set_left_click_callback(
        self, callback: Callable[[Player, Position], None]
    ) -> None:
        self._left_click_callback = callback
