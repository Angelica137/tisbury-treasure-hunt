from scripts.tuples import *


def test_get_coordinate():
    assert get_coordinate(("Scrimshaw Whale's Tooth", "2A")) == "2A"


def test_convert_coordinate():
    assert convert_coordinate("2A") == ("2", "A")


def test_compare_records():
    list_one_info = ('Brass Spyglass', '4B')
    list_two_info = ('Seaside Cottages', ('1', 'C'), 'blue')
    assert compare_records(list_one_info, list_two_info) == False


def test_compare_records_True():
    list_one_info = ('Model Ship in Large Bottle', '8A')
    list_two_info = ('Harbor Managers Office', ('8', 'A'), 'purple')
    assert compare_records(list_one_info, list_two_info) == True
