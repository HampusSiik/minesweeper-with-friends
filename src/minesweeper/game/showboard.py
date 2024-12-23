from typing import List, Dict, Optional

from minesweeper.board.board import Board
from minesweeper.game.showcell import ShowCell
from minesweeper.position import Position


class ShowBoard:
    """
    ShowBoard is a class that represents the board that the player sees.
    It is a 2D array of ShowCell objects.
    """

    _board: List[List[ShowCell]]
    """
    _board is a 2D array of ShowCell objects.
    """

    def __init__(self, board: Board):
        """
        Initializes a ShowBoard object with the given Board object.

        Args:
            board (Board): The Board object to be shown.
        """

        rows, cols = board.shape()

        def make_show_cell(pos: Position) -> ShowCell:
            """
            Creates a ShowCell object based on the given Position object.
            """
            adjacent_mines = board.surrounding_mines(pos)
            is_mine = board.is_mine(pos)
            is_flagged = board.is_flagged(pos)
            is_revealed = board.is_revealed(pos)
            if is_revealed:
                return ShowCell(adjacent_mines, is_mine, is_flagged, is_revealed)
            return ShowCell(None, None, is_flagged, is_revealed)

        self._board = [
            [make_show_cell((i, j)) for j in range(cols)] for i in range(rows)
        ]

    def get_board(self) -> List[List[ShowCell]]:
        """
        Returns the 2D array of ShowCell objects.

        Returns:
            List[List[ShowCell]]: The 2D array of ShowCell objects.
        """
        return self._board

    def show(self) -> str:
        """
        Returns stringrepresentation of the ShowBoard object.

        Returns:
            str: String representation of the ShowBoard object.
        """
        return "\n".join(" ".join(str(cell) for cell in row) for row in self._board)

    def to_dict(self) -> List[List[Dict[str, Optional[bool | int]]]]:
        """
        Converts the ShowBoard object to a dictionary that can be serialized into JSON.

        Returns:
            Dict[str, Any]: The dictionary representation of the ShowBoard object.
        """
        return [[cell.to_dict() for cell in row] for row in self._board]
