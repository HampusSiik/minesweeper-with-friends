from typing import Dict, Optional, Any
from flask import request, redirect, render_template

from minesweeper.position import from_dict
from minesweeper_room.roomapi import GameOptions, Player
from .api_app import app, session, room_api, players


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

    if not session.get("player"):
        return redirect("/login")

    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login() -> Any:
    """
    Set the player name.
    """

    request_data: Optional[Dict[str, str]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    username = request_data.get("username")
    if not username:
        return {"error": "Invalid data provided."}, 400

    players[username] = Player(username)

    session["player"] = username
    return redirect("/")


@app.route("/login", methods=["GET"])
def get_login() -> Any:
    """
    Get the login page.
    """

    return render_template("login.html")


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

    return {"room_id": room_id}


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

    room_api.join_room(room_id, players.get(player, Player(player)))
    return render_template("room.html", room_id=room_id, player_name=player)


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
        room_api.leave_room(room_id, players.get(player, Player(player)))

    return redirect("/")


@app.route("/left_click", methods=["POST"])
def left_click() -> Any:
    """
    Handle the left click event.
    """

    username: Optional[str] = session.get("player")
    if not username:
        return _no_player()

    request_data: Optional[Dict[str, Any]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    position = from_dict(request_data["position"])

    player: Player = players.get(username, Player(username))

    player.left_click(position)

    return "", 204


@app.route("/right_click", methods=["POST"])
def right_click() -> Any:
    """
    Handle the right click event.
    """

    username: Optional[str] = session.get("player")
    if not username:
        return _no_player()

    player: Optional[Player] = players.get(username)

    if not player:
        return _no_player()

    request_data: Optional[Dict[str, Any]] = request.json
    if not request_data:
        return {"error": "No data provided."}, 400

    position = from_dict(request_data["position"])

    player.right_click(position)

    return "", 204


@app.route("/reset", methods=["POST"])
def reset() -> Any:
    """
    Reset the game.
    """

    username: Optional[str] = session.get("player")
    if not username:
        return _no_player()

    player: Optional[Player] = players.get(username)

    if not player:
        return _no_player()

    player.reset_game()

    return "", 204


@app.route("/logout", methods=["POST"])
def logout() -> Any:
    """
    Logout the player.
    """
    username = session.get("player")
    if username is not None:
        players.pop(username, None)

    session.pop("player", None)
    return redirect("/")
