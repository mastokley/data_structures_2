import pytest

TEST_TRIE = {
    "a": {"b": {"o": {"u": {"t": {"$": ""}}}},
          "s": {'$': ""}},
    "t": {"h": {"a": {"t": {"$": "",
                            "'": {"s": {"$": ""}}}},
                "e": {"$": "",
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


def test_trie_traversal():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    output = [w for w in trie.traversal()]
    expected = ['about', 'as', 'the', "that's", 'them', 'that']
    assert sorted(expected) == sorted(output)


def test_trie_traversal_edge_zero():
    from .trie import Trie
    trie = Trie()
    output = [w for w in trie.traversal()]
    expected = []
    assert sorted(expected) == sorted(output)


def test_trie_traversal_subset():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    output = [w for w in trie.autocomplete('th')]
    expected = ['the', "that's", 'them', 'that']
    assert sorted(expected) == sorted(output)


def test_autocomplete_mulitlist():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    out = trie.autocomplete_multilist("that's")
    expected = {
        't': sorted(['the', "that's", 'them', 'that']),
        'th': sorted(['the', "that's", 'them', 'that']),
        'tha': sorted(["that's", 'that']),
        'that': sorted(["that's", 'that']),
        "that'": sorted(["that's"]),
        "that's": sorted(["that's"]),
    }
    assert out == expected


def test_autocomplete_mulitlist_2():
    from .trie import Trie
    trie = Trie()
    trie._container = TEST_TRIE
    out = trie.autocomplete_multilist("that'sss")
    expected = {
        't': sorted(['the', "that's", 'them', 'that']),
        'th': sorted(['the', "that's", 'them', 'that']),
        'tha': sorted(["that's", 'that']),
        'that': sorted(["that's", 'that']),
        "that'": sorted(["that's"]),
        "that's": sorted(["that's"]),
        "that'ss": sorted([]),
        "that'sss": sorted([]),
    }
    assert out == expected
