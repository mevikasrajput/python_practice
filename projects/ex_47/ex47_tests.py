from nose.tools import *
from game import Room

def test_room():
    gold = Room("GoldRoom", 
                """This room has gold in it.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, [])

def test_room_paths():
    center = Room("center", "Test room in the center.")
    north = Room("north", "Test room in the north.")
    south = Room("south", "Test room in the south")

    center.add_paths({'north': north, 'south' : south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south', south))

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's a dark down here, you can go up.")

    start.add_paths({'west': west, 'down':down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    asserrt_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
