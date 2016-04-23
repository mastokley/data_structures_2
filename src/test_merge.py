import pytest
import itertools as it

MERGE_PARAMS = [
    ([0], [], [0]),
    ([], [0], [0]),
    ([1], [0], [0, 1]),
    ([1, 3], [0], [0, 1, 3]),
    ([1], [0, 3], [0, 1, 3]),
    ([1, 2], [0, 3, 4], [0, 1, 2, 3, 4]),
    ([1, 2, 5], [0, 3, 4], [0, 1, 2, 3, 4, 5]),

]

MERGE_SORT_PARAMS = [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([2, 1], [1, 2]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 3, 2], [1, 2, 3]),
    ([2, 1, 3], [1, 2, 3]),
    ([2, 3, 1], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([3, 1, 2], [1, 2, 3]),
]


@pytest.mark.parametrize(('in1', 'in2', 'expected'), MERGE_PARAMS)
def test_merge(in1, in2, expected):
    from merge import merge
    assert merge(in1, in2) == expected


@pytest.mark.parametrize(('inlist', 'expected'), MERGE_SORT_PARAMS)
def test_merge_sort(inlist, expected):
    from merge import merge_sort
    assert merge_sort(inlist) == expected


def test_merge_sort_bluntly():
    """Takes some time to run."""
    # 3,628,800 for 10 nPr 10
    from merge import merge_sort
    for permutation in it.permutations(range(5)):
        expected = [x for x in range(5)]
        assert merge_sort([*permutation]) == expected
