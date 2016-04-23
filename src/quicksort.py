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
            left = [max(iterable)]
            right = [min(iterable)]
        else:
            left, right = [], []
            for item in iterable:
                right.append(item) if item > pivot else left.append(item)
        for element in quicksort(left):
            yield element
        for element in quicksort(right):
            yield element
