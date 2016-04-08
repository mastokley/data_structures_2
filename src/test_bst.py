import pytest

DIVERSE_TREES = [
    [1, 2, 3, 5, ],
    [2, 4, 6, 8, ],
    [17, 1, 23, 100, 5, ],
    [0, 0, 34, 0, 33, ],
    [22 , 2, 6, -7, 31, 5, 18, 
    14, 108, -54, 24.5, 
    29, -23, 16],
]


@pytest.fixture
def empty_tree():
    from bst import BST
    empty_tree = BST()
    return empty_tree


# @pytest.fixture
# def loaded_tree():
#     from bst import BST
#     loaded_tree = BST()
#     for item in DIVERSE_TREES[num]:
#         loaded_tree.insert(item)
#     return loaded_tree

def _load_tree(tree, num):
    for item in DIVERSE_TREES[num]:
        tree.insert(item)
    return tree

def test_insert(empty_tree):
    empty_tree.insert(10)
    assert empty_tree.head.val == 10


def test_insert_multiple(empty_tree):
    empty_tree.insert(10)
    empty_tree.insert(10)
    assert empty_tree.head.r_child is None
    assert empty_tree.head.l_child is None


def test_insert_multiple_diverse(empty_tree):
    empty_tree.insert(10)
    empty_tree.insert(20)
    assert empty_tree.head.r_child is not None
    assert empty_tree.head.l_child is None


def test_contains_empty(empty_tree):
    assert not empty_tree.contains(5)


def test_contains_positive(empty_tree):
    tree = _load_tree(empty_tree, 0)
    result = tree.contains(5)
    assert result


def test_contains_positive_2(empty_tree):
    tree = _load_tree(empty_tree, 3)
    result = tree.contains(5)
    assert not result


def test_size_empty(empty_tree):
    assert empty_tree.size() == 0


def test_size(empty_tree):
    empty_tree.insert(777)
    assert empty_tree.size() == 1


def test_size_multiple(empty_tree):
    empty_tree.insert(777)
    empty_tree.insert(778)
    assert empty_tree.size() == 2


def test_depth_empty(empty_tree):
    assert empty_tree.depth() == 0


def test_depth(empty_tree):
    empty_tree.insert(5)
    assert empty_tree.depth() == 1


def test_depth_full(empty_tree):
    empty_tree.insert(5)
    empty_tree.insert(6)
    assert empty_tree.depth() == 2


def test_depth_full_2(empty_tree):
    empty_tree.insert(5)
    empty_tree.insert(7)
    empty_tree.insert(6)
    assert empty_tree.depth() == 3


def test_depth_full_craggy(empty_tree):
    for val in [2, 3, 4, 1, 10, 11, 12, 7, 8, 9, ]:
        empty_tree.insert(val)
    assert empty_tree.depth() == 7


def test_depth_no_right(empty_tree):
    for val in [12, 3, 4, 1, 10, 11, 2, 7, 8, 9, ]:
        empty_tree.insert(val)
    assert empty_tree.depth() == 7

def test_balance_0(empty_tree):
    tree = _load_tree(empty_tree, 0)
    import pdb; pdb.set_trace()
    assert tree.balance() == -3


def test_balance_general(empty_tree):
    tree = _load_tree(empty_tree, 4)
    assert tree.balance() == tree.depth(tree.head.l_child) - tree.depth(tree.head.r_child)


def test_balance_empty(empty_tree):
    tree = empty_tree
    assert tree.balance() == 0


def test_balance_head(empty_tree):
    tree = empty_tree
    tree.insert(5)
    assert tree.balance() == 0
