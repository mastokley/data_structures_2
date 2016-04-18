
import io
import pytest

with io.open('../data/american-english-small') as file:
    WORDS = file.read()


@pytest.fixture
def empty_hash_table(scope='function'):
    from hash_table import HashTable
    hash_table = HashTable()


def test_instantiation(hash_table):
    """"""
    assert False


def test_set():
    """"""

