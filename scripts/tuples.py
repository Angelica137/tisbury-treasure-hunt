def get_coordinate(item: tuple) -> str:
    """
    :return: the map coordinate from the treasure, coordinate tuple
    """
    return item[-1]


def convert_coordinate(coordinate: str) -> tuple:
    """
    :return: tuple containing a number-letter pair from coordinate
    """
    return tuple(coordinate)


def compare_records(list_one_info: tuple, list_two_info: tuple) -> bool:
    """
    Checks if coordinates in each tuple match
    """
    list_one_coordinate = convert_coordinate(get_coordinate(list_one_info))
    return list_one_coordinate in list_two_info
