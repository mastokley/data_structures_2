from collections import deque


def merge_sort(list_):
    if len(list_) > 1:
        pivot = len(list_) >> 1
        left, right = list_[:pivot], list_[pivot:]
        return merge(merge_sort(left), merge_sort(right))
    return list_


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


