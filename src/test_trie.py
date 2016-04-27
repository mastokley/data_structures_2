import pytest

TEST_TRIE = {
    "a": {
        "b": {"o":{"u": {"t": {"$": ""}}}}, 
        "s": {'$': ""}
    },
    "t": {"h": {
            "a":{"t": {
                "$": "", 
                "'": {"s": {"$": ""}}}}, 
            "e": {
                "$": "", 
                "m": {"$": ""}}}} 
}

def test_insert():
    from .trie import Trie
    trie = Trie()
    trie.insert('as')
    trie.insert('about')
    trie.insert('the')
    trie.insert("that's")
    trie.insert("that")
    trie.insert("them")
    trie.insert("them")

    assert trie._container == TEST_TRIE

def test_contains():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    assert trie.contains('as')
    assert trie.contains('about')
    assert trie.contains('that')
    assert trie.contains('them')
    assert trie.contains("that's")
    assert not trie.contains("bad")
    assert not trie.contains("abo")

def test_empty_trie():
    from .trie import Trie
    trie = Trie()
    assert not trie.contains('false')

def test_not_a_string():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    with pytest.raises(TypeError):
        trie.contains(23)

def test_invalid_string():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    with pytest.raises(TypeError):
        trie.contains('23')



