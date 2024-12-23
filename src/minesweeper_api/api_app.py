from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, emit
from typing import Dict, Any, Optional
from minesweeper.game.minesweeper import Minesweeper
from minesweeper.position import Position, from_dict

# Flask app setup
app = Flask(__name__)
"""
The `app` object is the Flask application that will handle HTTP requests.
"""
app.config["SECRET_KEY"] = "supersecretkey"
socketio = SocketIO(app, cors_allowed_origins="*")
"""
The `socketio` object is the Flask-SocketIO extension that will handle WebSocket connections.
"""

# Store active games
games: Dict[str, Minesweeper] = {}


@app.route("/create_game", methods=["POST"])
def create_game() -> Any:
    """
    Create a new Minesweeper game.
    Expects JSON with 'rows', 'cols', and 'mines'.
    Returns the game ID.
    """
    data: Optional[Dict[str, int]] = request.json
    if data is None:
        return jsonify({"error": "Invalid input"}), 400
    rows: int = data["rows"]
    cols: int = data["cols"]
    mines: int = data["mines"]
    game_id: str = f"game_{len(games) + 1}"  # Generate a unique ID
    game: Minesweeper = Minesweeper()
    game.generate_game(rows, cols, mines)
    games[game_id] = game
    return jsonify({"game_id": game_id})


@app.route("/get_board/<game_id>", methods=["GET"])
def get_board(game_id: str) -> Any:
    """
    Retrieve the current board state of a game.
    """
    game: Optional[Minesweeper] = games.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    return jsonify({"board": game.get_show_board().to_dict()})


@socketio.on("join_game")
def handle_join_game(data: Dict[str, Any]) -> None:
    """
    Handle a player joining a game room.
    """
    game_id: str = data["game_id"]
    join_room(game_id)
    emit("message", {"msg": f"Player joined {game_id}"}, to=game_id, broadcast=True)


def update_board(game_id: str) -> None:
    """
    Helper function to broadcast the updated board to all players in a game.
    """
    game: Optional[Minesweeper] = games.get(game_id)
    if game:
        board = game.get_show_board().to_dict()
        emit("update_board", {"board": board}, to=game_id)


@socketio.on("left_click")
def handle_left_click(data: Dict[str, Any]) -> None:
    """
    Handle a left-click action in the game.
    Updates the game state and broadcasts the updated board.
    """
    game_id: str = data["game_id"]
    position: Position = from_dict(data["position"])
    game: Optional[Minesweeper] = games.get(game_id)
    if game:
        game.left_click_cell(position)
        update_board(game_id)


@socketio.on("right_click")
def handle_right_click(data: Dict[str, Any]) -> None:
    """
    Handle a right-click action in the game.
    Updates the game state and broadcasts the updated board.
    """
    game_id: str = data["game_id"]
    position: Position = from_dict(data["position"])
    game: Optional[Minesweeper] = games.get(game_id)
    if game:
        game.right_click_cell(position)
        update_board(game_id)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
