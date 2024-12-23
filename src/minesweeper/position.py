from typing import Tuple


Position = Tuple[int, int]
"""
Represents a position on the board.
"""


def from_dict(data: dict) -> Position:
    """
    Converts a dictionary to a Position tuple.

    Args:
        data (dict): The dictionary to convert.

    Returns:
        Position: The Position tuple.
    """
    return data["row"], data["col"]
