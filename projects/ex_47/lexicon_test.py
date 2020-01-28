from nose.tools import *
from ex_47 import lexicon

def test_direction():
    assert_equal(lexicon.scan("north"), [("direction, 'north")])
    result = lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", "south"),                               
                          ("direction", "east")])

def test_stop():
    assert_equal(lexicon.scan("the"), [("stop", "the")])
    result = lexicon.scan("in the of")
    assert_equal(result, [("stop", "the"),
                          ("stop", "in"),
                          ("stop", "of")])

def test_verb():
    assert_equal(lexicon.scan("go"), [("verb", go)])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [("verb", "go"),
                          ("verb", "kill"),
                          ("verb", "eat")])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [("stop", "bear")])
    result = lexicon.scan("bear princess")
    assert_equal(result, [("nouns", "bear"),
                          ("nouns", "princess")])


def test_numbers():
    assert_equal(lexicon.scan(1234), [("numbers", 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [("numbers", 3),
                          ("numbers", 91234])

                        
def test_errors():
    assert_equal(lexicon.scan("DFSDFSDFS"), [("error", "SFSDGFDFGDFG")])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [("noun", "bear"),
                          ("error", "IAS"),
                          ("noun", "princess")])
