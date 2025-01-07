from typing import Dict
from flask_socketio import emit, join_room, leave_room

from .api_app import socketio, room_api


@socketio.on("join_room")
def handle_join_room(data: Dict[str, str]) -> None:
    """
    Handle a player joining a room.
    """
    room_id: str = data["room_id"]
    join_room(room_id)
    emit("message", {"msg": f"Player joined {room_id}"}, to=room_id, broadcast=True)
    emit(
        "update_room",
        room_api.get_room_state(room_id).to_dict(),
        to=room_id,
    )


@socketio.on("leave_room")
def handle_leave_room(data: Dict[str, str]) -> None:
    """
    Handle a player leaving a room.
    """
    room_id: str = data["room_id"]
    leave_room(room_id)
    emit("message", {"msg": f"Player left {room_id}"}, to=room_id, broadcast=True)
    emit(
        "update_room",
        room_api.get_room_state(room_id).to_dict(),
        to=room_id,
    )


def update_room(room_id: str) -> None:
    """
    Update the room.
    """
    print(f"Updating room {room_id}")
    socketio.emit(
        "update_room",
        room_api.get_room_state(room_id).to_dict(),
        to=room_id,
    )


room_api.add_update_observer(update_room)
