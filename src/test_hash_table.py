
import io
import pytest

with io.open('../data/american-english-small') as file:
    WORDS = file.read()


@pytest.fixture
def empty_hash_table(scope='function'):
    from hash_table import HashTable
    ht = HashTable()
    return ht


@pytest.fixture
def full_hash_table(scope='function'):
    from hash_table import HashTable
    ht = HashTable()
    ht.set("apple", 1)
    ht.set("banana", 2)
    ht.set("crabapple", 3)
    ht.set("Abraheem van Helsing", "dog")
    ht.set("Special Agent Dale Cooper, FBI", "dog")
    ht.set("Oscar", "cat")
    return ht


def test_size_empty(empty_hash_table):
    """Assert size defaults to 1024."""
    assert empty_hash_table._size == 1024


def test_size_full(full_hash_table):
    """Assert size remains 1024."""
    assert full_hash_table._size == 1024


def test_table_instantiation(empty_hash_table):
    """Assert container instantiating."""
    expected = [[] for i in range(empty_hash_table._size)]
    assert empty_hash_table._container == expected


def test_get(full_hash_table):
    assert full_hash_table.get('apple') == 1


