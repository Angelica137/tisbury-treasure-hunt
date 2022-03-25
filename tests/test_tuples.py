from scripts.tuples import *


def test_get_coordinate():
    assert get_coordinate(("Scrimshaw Whale's Tooth", "2A")) == "2A"


def test_convert_coordinate():
    assert convert_coordinate("2A") == ("2", "A")


def test_compare_records():
    list_one_item = ('Brass Spyglass', '4B')
    list_two_item = ('Seaside Cottages', ('1', 'C'), 'blue')
    assert compare_records(list_one_item, list_two_item) == False


def test_compare_records_True():
    list_one_item = ('Model Ship in Large Bottle', '8A')
    list_two_item = ('Harbor Managers Office', ('8', 'A'), 'purple')
    assert compare_records(list_one_item, list_two_item) == True


def test_create_record():
    list_one_item = ('Brass Spyglass', '4B')
    list_two_item = ('Abandoned Lighthouse', ('4', 'B'), 'Blue')
    assert create_record(list_one_item, list_two_item) == (
        'Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')


def test_create_record_no_match():
    list_one_item = ('Brass Spyglass', '4B')
    list_two_item = (('1', 'C'), 'Seaside Cottages', 'blue')
    assert create_record(list_one_item, list_two_item) == "not a match"


def test_clean_up():
    items = ((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E',
                                                                                     'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))
    assert clean_up(items) == "('Brass Spyglass', 'Abandoned Lighthouse', ('4', 'B'), 'Blue')\n('Vintage Pirate Hat', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange')\n"
