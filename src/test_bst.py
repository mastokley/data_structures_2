import pytest

DIVERSE_TREES = [
    [1, 2, 3, 5, ],
    [2, 4, 6, 8, ],
    [17, 1, 23, 100, 5, ],
    [0, 0, 34, 0, 33, ],
    [22, 2, 6, -7, 31, 5, 18, 14, 108, -54, 24.5, 29, -23, 16],
]

@pytest.fixture
def empty_tree():
    from bst import BST
    empty_tree = BST()
    return empty_tree


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


def test_traversal_in(empty_tree):
    tree = _load_tree(empty_tree, 2)
    return_val = [x for x in tree.traverse_in()]
    assert return_val == [1, 5, 17, 23, 100]


def test_traversal_pre(empty_tree):
    tree = _load_tree(empty_tree, 2)
    return_val = [x for x in tree.traverse_pre()]
    assert return_val == [17, 1, 5, 23, 100]


def test_traversal_post(empty_tree):
    tree = _load_tree(empty_tree, 2)
    return_val = [x for x in tree.traverse_post()]
    assert return_val == [5, 1, 100, 23, 17]


def test_traversal_breadth(empty_tree):
    tree = _load_tree(empty_tree, 2)
    return_val = [x for x in tree.traverse_breadth()]
    assert return_val == [17, 1, 23, 5, 100]


def test_traversal_in_edge_zero(empty_tree):
    result = [x for x in empty_tree.traverse_in()]
    assert result == []


def test_traversal_pre_edge_zero(empty_tree):
    result = [x for x in empty_tree.traverse_pre()]
    assert result == []


def test_traversal_post_edge_zero(empty_tree):
    result = [x for x in empty_tree.traverse_post()]
    assert result == []


def test_traversal_breadth_edge_zero(empty_tree):
    result = [x for x in empty_tree.traverse_breadth()]
    assert result == []


def test_traversal_in_edge_one(empty_tree):
    empty_tree.insert(1000)
    result = [x for x in empty_tree.traverse_in()]
    assert result == [1000]


def test_traversal_pre_edge_one(empty_tree):
    empty_tree.insert(1000)
    result = [x for x in empty_tree.traverse_pre()]
    assert result == [1000]


def test_traversal_post_edge_one(empty_tree):
    empty_tree.insert(1000)
    result = [x for x in empty_tree.traverse_post()]
    assert result == [1000]


def test_traversal_breadth_edge_one(empty_tree):
    empty_tree.insert(1000)
    result = [x for x in empty_tree.traverse_breadth()]
    assert result == [1000]
