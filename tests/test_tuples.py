from scripts.tuples import *


def test_get_coordinate():
    assert get_coordinate(("Scrimshaw Whale's Tooth", "2A")) == "2A"
