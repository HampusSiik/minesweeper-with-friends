from typing import Dict


class GameOptions:
    """
    Represents the options for a Minesweeper game.
    """

    _mines: int
    """
    The number of mines in the game.
    """

    _width: int
    """
    The width of the game board.
    """

    _height: int
    """
    The height of the game board.
    """

    def __init__(self, mines: int, width: int, height: int) -> None:
        """
        Initializes a new GameOptions object.
        """
        self._mines = mines
        self._width = width
        self._height = height

    def mines(self) -> int:
        """
        Returns the number of mines in the game.

        Returns:
            int: The number of mines.
        """
        return self._mines

    def width(self) -> int:
        """
        Returns the width of the game board.

        Returns:
            int: The width of the game board.
        """
        return self._width

    def height(self) -> int:
        """
        Returns the height of the game board.

        Returns:
            int: The height of the game board.
        """
        return self._height

    def to_dict(self) -> Dict[str, int]:
        """
        Converts the GameOptions object to a dictionary.

        Returns:
            Dict[str, int]: The dictionary representation of the GameOptions object.
        """
        return {
            "mines": self._mines,
            "width": self._width,
            "height": self._height,
        }
