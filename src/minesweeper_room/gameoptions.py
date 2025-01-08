from typing import Dict


class GameOptions:
    """
    Represents the options for a Minesweeper game.
    """

    _mines: int
    """
    The number of mines in the game.
    """

    _cols: int
    """
    The width of the game board.
    """

    _rows: int
    """
    The height of the game board.
    """

    def __init__(self, mines: int, width: int, height: int) -> None:
        """
        Initializes a new GameOptions object.
        """
        self._mines = mines
        self._cols = width
        self._rows = height

    def mines(self) -> int:
        """
        Returns the number of mines in the game.

        Returns:
            int: The number of mines.
        """
        return self._mines

    def cols(self) -> int:
        """
        Returns the width of the game board.

        Returns:
            int: The width of the game board.
        """
        return self._cols

    def rows(self) -> int:
        """
        Returns the height of the game board.

        Returns:
            int: The height of the game board.
        """
        return self._rows

    def to_dict(self) -> Dict[str, int]:
        """
        Converts the GameOptions object to a dictionary.

        Returns:
            Dict[str, int]: The dictionary representation of the GameOptions.
        """
        return {
            "mines": self._mines,
            "cols": self._cols,
            "rows": self._rows,
        }
