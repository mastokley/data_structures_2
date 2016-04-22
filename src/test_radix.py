import pytest
import itertools as it
# from .test_insertion import Newple

# npl_a = Newple([1,1])
# npl_b = Newple([2,5])
# npl_c = Newple([2,0])

RADIX_PARAMS = [
    ([0], [], [0]),
    ([], [0], [0]),
    ([1], [0], [0, 1]),
    ([1, 3], [0], [0, 1, 3]),
    ([1], [0, 3], [0, 1, 3]),
    ([1, 2], [0, 3, 4], [0, 1, 2, 3, 4]),
    ([1, 2, 5], [0, 3, 4], [0, 1, 2, 3, 4, 5]),

]

RADIX_SORT_PARAMS = [
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
    # ([npl_a, npl_b, npl_c,], [npl_a, npl_b, npl_c,]),
]


# @pytest.mark.parametrize(('in1', 'in2', 'expected'), RADIX_PARAMS)
# def test_radix(in1, in2, expected):
#     from radix import radix
#     assert radix(in1, in2) == expected


@pytest.mark.parametrize(('inlist', 'expected'), RADIX_SORT_PARAMS)
def test_radix_sort(inlist, expected):
    from radix import radix_sort
    assert radix_sort(inlist) == expected


def test_radix_sort_bluntly():
    """Takes some time to run."""
    # 3,628,800 for 10 nPr 10
    from radix import radix_sort
    for permutation in it.permutations(range(5)):
        expected = [x for x in range(5)]
        assert radix_sort([*permutation]) == expected

