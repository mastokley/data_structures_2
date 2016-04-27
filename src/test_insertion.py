# _*_ Coding: Utf-8 _*_
import pytest

class Newple(tuple):
    """This class looks like a tuple but only compares 
    the first values for gt and lt operators."""

    def __gt__(self, newple):
        return self[0] > newple[0]

    def __lt__(self, newple):
        return self[0] < newple[0]

npl_a = Newple([1,1])
npl_b = Newple([2,5])
npl_c = Newple([2,0])

TEST_LIST = [
                    ([1, 3, 2, -20, 36, 18, 100, -12, 3.2, 3.2, 1], 
                        [-20, -12, 1, 1, 2, 3, 3.2, 3.2, 18, 36, 100 ]),
                    ([], []),
                    ([1], [1]),
                    ([npl_a, npl_b, npl_c,], [npl_a, npl_b, npl_c,]),
                ]




def test_newple_1():
    n1 = Newple([1, 2])
    n2 = Newple([2, 1])
    assert n1 < n2

def test_newple_2():
    n1 = Newple([2, 1])
    n2 = Newple([2, 2])
    assert not n1 < n2

@pytest.mark.parametrize(('input', 'expected'), TEST_LIST)
def test_insertion(input, expected):
    from .insertion import insert_sort
    assert insert_sort(input) == expected

# @pytest.mark.parametrize(('input', 'expected'), TEST_LIST)
# def test_insertion(input, expected):
#     from insertion import insert_sort
#     insert_sort(input)
#     assert input == expected




