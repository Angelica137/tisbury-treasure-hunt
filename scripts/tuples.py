def get_coordinate(item: tuple) -> str:
    """
    :return: the map coordinate from the treasure, coordinate tuple
    """
    return item[-1]


def convert_coordinate(coordinate: str) -> tuple:
    return tuple(coordinate)
