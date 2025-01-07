from typing import Dict, Optional, Any
from flask import request, redirect

from minesweeper.position import from_dict
from minesweeper_room.roomapi import GameOptions, Player
from .api_app import app, session, room_api


def _no_player() -> Any:
    """
    Handles the case where no player is set.
    """

    return redirect("/login")


def _not_implemented() -> Any:
    """
    Handles the case where the endpoint is not implemented.
    """

    return {"error": "Not implemented."}, 501


@app.route("/", methods=["GET"])
def index() -> Any:
    """
    Get the index page.
    """

    return _not_implemented()


@app.route("/login", methods=["POST"])
def login() -> Any:
    """
    Set the player name.
    """

    request_data: Optional[Dict[str, str]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    player = request_data.get("player")
    if not player:
        return {"error": "Invalid data provided."}, 400

    session["player"] = Player(player)

    return redirect("/")


@app.route("/login", methods=["GET"])
def get_login() -> Any:
    """
    Get the login page.
    """

    return _not_implemented()


@app.route("/rooms", methods=["POST"])
def create_room() -> Any:
    """
    Create a new room.
    """

    player = session.get("player")
    if not player:
        return _no_player()

    request_data: Optional[Dict[str, str]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    mines = request_data.get("mines")
    cols = request_data.get("cols")
    rows = request_data.get("rows")

    if not mines or not cols or not rows:
        return {"error": "Invalid data provided."}, 400

    game_options = GameOptions(int(mines), int(cols), int(rows))

    room_id = room_api.create_room(game_options)

    return redirect(f"/rooms/{room_id}")


# join_room
@app.route("/rooms/<room_id>", methods=["GET"])
def get_room(room_id: str) -> Any:
    """
    Get the room data.

    Args:
        room_id (str): The room ID.
    """

    player = session.get("player")
    if not player:
        return _no_player()

    room_api.join_room(room_id, player)
    return _not_implemented()


# leave_room
@app.route("/rooms/<room_id>", methods=["DELETE"])
def leave_room(room_id: str) -> Any:
    """
    Leave the room.

    Args:
        room_id (str): The room ID.
    """

    player = session.get("player")
    if player is not None:
        room_api.leave_room(room_id, player)

    return redirect("/")


@app.route("/left_click", methods=["POST"])
def left_click() -> Any:
    """
    Handle the left click event.
    """

    player: Optional[Player] = session.get("player")
    if not player:
        return _no_player()

    request_data: Optional[Dict[str, int]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    position = from_dict(request_data)

    player.left_click(position)

    return "", 204


@app.route("/right_click", methods=["POST"])
def right_click() -> Any:
    """
    Handle the right click event.
    """

    player: Optional[Player] = session.get("player")
    if not player:
        return _no_player()

    request_data: Optional[Dict[str, int]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    position = from_dict(request_data)

    player.right_click(position)

    return "", 204


@app.route("/logout", methods=["POST"])
def logout() -> Any:
    """
    Logout the player.
    """

    session.pop("player", None)
    return redirect("/")
