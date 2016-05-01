def insert_sort(list_):
    """Take a list, return a sorted copy of the list"""
    outlist = list(list_)
    for outer_index in range(1, len(outlist)):
        inner_index = outer_index
        try:
            while outlist[inner_index] < outlist[inner_index - 1]:
                _swap(outlist, inner_index)
                inner_index -= 1
        except IndexError:
            pass
    return outlist


def _swap(list_, index):
    """Swap item with item at previous index."""
    list_[index], list_[index - 1] = list_[index - 1], list_[index]

"""This function allows a user to sort based upon an attribute or function key.
    We won't actually be using it but it is too cool to delete."""
# def keyed_insert_sort(list_, key=None):
#     outlist = list_
#     if key is None:
#         for outer_index in range(len(outlist)):
#             inner_index = outer_index
#             try:
#                 while outlist[outer_index] < outlist[inner_index - 1]:
#                     _swap(outlist, inner_index)
#                     inner_index -= 1
#             except IndexError:
#                 pass
#     # if key is passed in as string, can't use it to invoke attribute
#     elif hasattr(outlist[0], key):
#         for outer_index in range(len(outlist)):
#             inner_index = outer_index
#             try:
#                 while (getattr(outlist[outer_index], key) <
#                        getattr(outlist[inner_index - 1], key)):
#                     _swap(outlist, inner_index)
#                     inner_index -= 1
#             except IndexError:
#                 pass
#     elif hasattr(key, '__call__'):
#         for outer_index in range(len(outlist)):
#             inner_index = outer_index
#             try:
#                 while key(outlist[outer_index]) < key(outlist[inner_index - 1]):
#                     _swap(outlist, inner_index)
#                     inner_index -= 1
#             except IndexError:
#                 pass
#     return outlist
