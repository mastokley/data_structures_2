# _*_ Coding: Utf-8 _*_
import itertools
import math
from random import randint


def radix_sort(list_):
    if not list_:
        return list_
    max_ = max(list_)
    power = math.ceil(math.log(max_, 10))
    i_ = 0

    while i_ < power:
        yet_another_list = _power_sort(list_, i_)
        list_ = yet_another_list
        i_ += 1
    return list_


def _power_sort(other_list, num):
    sorted_list = [[] for i in range(10)]
    for item in other_list:
        sorted_list[(item // 10**num) % 10].append(item)
    return _unbin(sorted_list)


def _unbin(twodee_list):
    return list(itertools.chain.from_iterable(twodee_list))

"""This is AJ and Hannah's Code.  We raced and lost"""
# def radix_competitor(nums):
#     """Radix sort implementation."""
#     if not nums:
#         return nums
#     tens = 10
#     for iteration in range(len(str(max(nums)))):
#         buckets = [[] for x in range(10)]
#         for num in nums:
#             buckets[(num % tens) // (tens // 10)].append(num)
#         tens *= 10
#         nums = [num for li in buckets for num in li]
#     return nums


if __name__ == '__main__':
    from timeit import Timer
    input = [randint(0, 1000000) for i in range(500)]
    t = Timer(lambda: radix_sort(input))
    print("This radix sort has time complexity somewhere between O(wn) and O(w + N)")
    print("running a 500 item list 500 times")
    print(t.timeit(number=500))
    print("running a 50 item list 500 times")
    input = [randint(0, 1000000) for i in range(50)]
    t = Timer(lambda: radix_sort(input))
    print(t.timeit(number=500))
    """print("this is where AJ's crummy solution starts")"""
    # input = [randint(0, 1000000) for i in range(500)]
    # t = Timer(lambda: radix_competitor(input))
    # print("This radix sort has time complexity somewhere between O(wn) and O(w + N)")
    # print("running a 500 item list 500 times")
    # print(t.timeit(number=500))
    # print("running a 50 item list 500 times")
    # input = [randint(0, 1000000) for i in range(50)]
    # t = Timer(lambda: radix_competitor(input))
    # print(t.timeit(number=500))
