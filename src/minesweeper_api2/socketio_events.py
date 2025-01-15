from typing import Dict, Any
from flask_socketio import emit, join_room, leave_room

from .api_app import socketio, room_api, session, players
from minesweeper.position import from_dict


def update_room(room_id: str) -> None:
    """
    Update the room.
    """
    socketio.emit(
        "update_room",
        room_api.get_room_state(room_id).to_dict(),
        to=room_id,
    )


@socketio.on("join_room")
def handle_join_room(data: Dict[str, str]) -> None:
    """
    Handle a player joining a room.
    """
    room_id: str = data["room_id"]
    join_room(room_id)
    emit(
        "message",
        {"msg": f"Player joined {room_id}"},
        to=room_id,
        broadcast=True,
    )
    update_room(room_id)


@socketio.on("leave_room")
def handle_leave_room(data: Dict[str, str]) -> None:
    """
    Handle a player leaving a room.
    """
    room_id: str = data["room_id"]
    leave_room(room_id)
    emit(
        "message",
        {"msg": f"Player left {room_id}"},
        to=room_id,
        broadcast=True,
    )
    update_room(room_id)


def handle_click(event: str, data: Dict[str, Any]) -> None:
    """
    Handle a click event (left or right).
    """
    player_name = session.get("player")
    if player_name is None:
        return
    player = players.get(player_name)
    if player is None:
        return
    position_dict = data.get("position")
    if position_dict is None:
        return
    position = from_dict(position_dict)

    if event == "left_click":
        player.left_click(position)
    elif event == "right_click":
        player.right_click(position)


@socketio.on("left_click")
def handle_left_click(data: Dict[str, Any]) -> None:
    """
    Handle a left click event.
    """
    handle_click("left_click", data)


@socketio.on("right_click")
def handle_right_click(data: Dict[str, Any]) -> None:
    """
    Handle a right click event.
    """
    handle_click("right_click", data)


@socketio.on("reset_game")
def handle_reset(_) -> None:
    """
    Handle a reset game event.
    """
    player_name = session.get("player")
    if player_name is None:
        return
    player = players.get(player_name)
    if player is None:
        return
    player.reset_game()


room_api.add_update_observer(update_room)
