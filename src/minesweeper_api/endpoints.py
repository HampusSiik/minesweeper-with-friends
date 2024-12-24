from flask import request, jsonify, render_template
from typing import Dict, Any, Optional
from minesweeper_api.api_app import app, games
from minesweeper.game.minesweeper import Minesweeper


@app.route("/", methods=["GET"])
def home() -> Any:
    return render_template("main-menu.html")


@app.route("/game/<game_id>", methods=["GET"])
def game(game_id: str) -> Any:
    return render_template("game.html")


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
