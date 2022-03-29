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


def compare_records(list_one_item: tuple, list_two_item: tuple) -> bool:
    """
    Checks if coordinates in each tuple match
    """
    list_one_coordinate = convert_coordinate(get_coordinate(list_one_item))
    return list_one_coordinate in list_two_item


def create_record(list_one_item: tuple, list_two_item: tuple) -> tuple:
    """
    Checks if coordinates match for the items passed
    If they do, returns tuple with all info from both parameters
    If not, returns "not a match"
    """
    if compare_records(list_one_item, list_two_item):
        return list_one_item + list_two_item
    return "not a match"


def clean_up(items: tuple) -> str:
    """
    :param items: tuple - contains tuples of with the all data for one item from both lists
    :return repot: str - each item is returned on its own line with coordinate in format "E2"
    removed
    """
    report = []
    for item in items:
        clean_tuple = tuple(item[:1] + item[2:])
        report.append(clean_tuple)
    return ('\n'.join(map(str, report)))+'\n'
