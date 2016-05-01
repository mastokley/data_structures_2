from random import randint

import numpy


def quicksort(iterable):
    """Return a generator object which will yield elements in order."""
    if len(iterable) < 2:
        for item in iterable:
            yield item
    else:
        first, last = iterable[0], iterable[-1]
        middle = iterable[len(iterable) // 2]
        pivot = numpy.median([first, last, middle])
        if len(iterable) == 2:
            left = [min(iterable)]
            right = [max(iterable)]
        else:
            left, right = [], []
            for item in iterable:
                right.append(item) if item > pivot else left.append(item)
        for element in quicksort(left):
            yield element
        for element in quicksort(right):
            yield element

if __name__ == '__main__':
    from timeit import Timer
    input = [randint(0, 1000000) for i in range(500)]
    t = Timer(lambda: quicksort(input))
    print("This quicksort has time complexity average complexity O(n log n) and worst case complexity O(n^2)")
    print("running a 500 item list 500 times")
    print(t.timeit(number=500))
    print("running a 50 item list 500 times")
    input = [randint(0, 1000000) for i in range(50)]
    t = Timer(lambda: quicksort(input))
    print(t.timeit(number=500))
