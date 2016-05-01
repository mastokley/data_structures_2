# """Hash table."""


# class HashTable(object):
#     """Implementation of a hash table."""

#     def __init__(self, size=1024):
#         self._size = size
#         self._container = [[] for i in range(self._size)]

#     def get(self, key):
#         # doesn't handle bins/collisions
#         bin_, index = self._hash(key)
#         return self._container[bin_][index - 1]

#     def _hash(self, key):
#         bin_ = sum([ord(c) for c in key])
#         return bin_, len(self._container[bin_])

#     def set(self, key, value):
#         bin_, index = self._hash(key)
#         # should be inserting key, value pair but only if sharing
#         # bin with other key, value pair
#         self._container[bin_].insert(value)
