import itertools as it

import pytest

from .test_insertion import Newple

"""
The Newple is a subclass of tuple with its __gt__ and __lt__
methods overwritten to only compare the first value in each
Newple.  It allows for stability testing.
"""

npl_a = Newple([1, 1])
npl_b = Newple([2, 5])
npl_c = Newple([2, 0])

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
    ([npl_a, npl_b, npl_c, ], [npl_a, npl_b, npl_c, ]),
]


@pytest.mark.parametrize(('in1', 'in2', 'expected'), MERGE_PARAMS)
def test_merge(in1, in2, expected):
    from .merge import merge
    assert merge(in1, in2) == expected


@pytest.mark.parametrize(('inlist', 'expected'), MERGE_SORT_PARAMS)
def test_merge_sort(inlist, expected):
    from .merge import merge_sort
    assert merge_sort(inlist) == expected


def test_word_merge_sort():
    from .merge import merge_sort
    name_list = ['bobby', 'alex', 'janice']
    out_list = ['alex', 'bobby', 'janice']
    assert merge_sort(name_list) == out_list


def test_word_merge_negative_nums():
    from .merge import merge_sort
    name_list = [20, .5, -2]
    out_list = [-2, .5, 20]
    assert merge_sort(name_list) == out_list

# def test_merge_sort_bluntly():
#     """Takes some time to run."""
#     # 3,628,800 for 10 nPr 10
#     from .merge import merge_sort
#     for permutation in it.permutations(range(5)):
#         expected = [x for x in range(5)]
#         perms = [p for p in permutation]
#         assert merge_sort(perms) == expected
