import pytest

from .test_insertion import Newple

npl_a = Newple([1, 1])
npl_b = Newple([2, 5])
npl_c = Newple([2, 0])


PARAMS = [
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
    ([3, 0, 2], [0, 2, 3]),
    ([3, -1, 2], [-1, 2, 3]),
    ([3, -1, 2.5], [-1, 2.5, 3]),
    #   ([npl_a, npl_b, npl_c, ], [npl_a, npl_b, npl_c, ]),
]


@pytest.mark.parametrize(('inlist', 'expected'), PARAMS)
def test_sort(inlist, expected):
    from .quicksort import quicksort
    assert [x for x in quicksort(inlist)] == expected


@pytest.mark.parametrize(('inlist', 'expected'), PARAMS)
def test_unpacked_quicksort(inlist, expected):
    from .quicksort import unpacked_quicksort
    assert unpacked_quicksort(inlist) == expected


# def test_sort_bluntly():
#     """Takes some time to run."""
#     from quicksort import quicksort
#     for permutation in it.permutations(range(5)):
#         expected = [x for x in range(5)]
#         assert [x for x in quicksort([*permutation])] == expected
