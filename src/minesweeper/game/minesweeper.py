from typing import Tuple
from minesweeper.position import Position
from minesweeper.board.board import Board


class Minesweeper:
    """
    Minesweeper game.

    """

    _board: Board
    """
    Minesweeper board.
    """

    _mines: int
    """
    Number of mines on the board.
    """

    def __init__(self):
        """
        Initialize the game.
        """
        self._board = Board()

        self._mines = 0

    def shape(self) -> Tuple[int, int]:
        """
        Get the shape of the board.

        Returns:
            Tuple[int, int]: Shape of the board.
        """
        return self._board.shape()

    def game_lost(self) -> bool:
        """
        Check if the game is lost.

        Returns:
            bool: True if the game is lost, False otherwise.
        """
        return any(
            self._board.is_mine(position) and self._board.is_revealed(position)
            for position in self._board.all_positions()
        )

    def game_won(self) -> bool:
        """
        Check if the game is won.

        Returns:
            bool: True if the game is won, False otherwise.
        """
        return (
            all(
                self._board.is_mine(position) or self._board.is_revealed(position)
                for position in self._board.all_positions()
            )
            and not self.game_lost()
        )

    def left_click_cell(self, position: Position) -> None:
        """
        Left click a cell.

        Args:
            position (Position): Position to left click.
        """
        if self._board.mines() != self._mines:
            self.place_mines(self._mines, position)
        if self._board.is_flagged(position):
            return
        self._board.reveal(position)

    def right_click_cell(self, position: Position) -> None:
        """
        Right click a cell.

        Args:
            position (Position): Position to right click.
        """
        if self._board.is_revealed(position):
            return
        self._board.toggle_flag(position)

    def generate_game(self, rows: int, columns: int, mines: int) -> None:
        """
        Generate a board.

        Args:
            rows (int): Number of rows.
            columns (int): Number of columns.
        """
        self._board.generate_board(rows, columns)
        self._mines = mines

    def place_mines(self, num_mines: int, start_position: Position) -> None:
        """
        Place mines on the board.

        Args:
            num_mines (int): Number of mines to place.
            start_position (Position): Position to avoid placing mines.
        """
        self._board.place_mines(num_mines, start_position)
