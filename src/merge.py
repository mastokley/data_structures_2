from collections import deque
import timeit
from random import randint


def merge(list1, list2):
    outlist = []
    left = deque(list1)
    right = deque(list2)
    while left and right:
        if left[0] > right[0]:
            outlist.append(right.popleft())
        else:
            outlist.append(left.popleft())
    if left:
        outlist.extend(left)
    if right:
        outlist.extend(right)
    return outlist


def merge_sort(list_):
    if len(list_) > 1:
        pivot = len(list_) >> 1
        left, right = list_[:pivot], list_[pivot:]
        return merge(merge_sort(left), merge_sort(right))
    return list_


if __name__ == '__main__':
    from timeit import Timer
    input = [randint(0, 1000000) for i in range(500)]
    t = Timer(lambda: merge_sort(input))
    print("This merge sort has time complexity of O(n log n)")
    print("running a 500 item list 500 times")
    print(t.timeit(number=500))
    print("running a 50 item list 500 times")
    input = [randint(0, 1000000) for i in range(50)]
    t = Timer(lambda: merge_sort(input))
    print(t.timeit(number=500))