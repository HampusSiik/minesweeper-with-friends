from flask_socketio import join_room, emit
from typing import Dict, Any, Optional
from minesweeper_api.api_app import socketio, games
from minesweeper.position import Position, from_dict
from minesweeper.game.minesweeper import Minesweeper


def update_board(game_id: str) -> None:
    """
    Helper function to broadcast the updated board to all players in a game.
    """
    game: Optional[Minesweeper] = games.get(game_id)
    if game:
        board = game.get_show_board().to_dict()
        emit("update_board", {"board": board}, to=game_id)


@socketio.on("join_game")
def handle_join_game(data: Dict[str, Any]) -> None:
    """
    Handle a player joining a game room.
    """
    game_id: str = data["game_id"]
    join_room(game_id)
    emit("message", {"msg": f"Player joined {game_id}"}, to=game_id, broadcast=True)


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
