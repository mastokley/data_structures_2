def insert_sort(list_, key=None):
    if key is None:
        for outer_index in range(len(list_)):
            inner_index = outer_index
            try:
                while list_[outer_index] < list_[inner_index - 1]:
                    _swap(list_, inner_index)
                    inner_index -= 1
            except IndexError:
                pass
    # if key is passed in as string, can't use it to invoke attribute
    elif hasattr(list_[0], key):
        for outer_index in range(len(list_)):
            inner_index = outer_index
            try:
                while (getattr(list_[outer_index], key) <
                       getattr(list_[inner_index - 1], key)):
                    _swap(list_, inner_index)
                    inner_index -= 1
            except IndexError:
                pass
    elif hasattr(key, '__call__'):
        for outer_index in range(len(list_)):
            inner_index = outer_index
            try:
                while key(list_[outer_index]) < key(list_[inner_index - 1]):
                    _swap(list_, inner_index)
                    inner_index -= 1
            except IndexError:
                pass
    return list_

    # attempt at pythonic idiom

    # for index, item in enumerate(unique_list):
    #     inner_index = index
    #     while item[0] < unique_list[inner_index - 1][0]:
    #         _swap(unique_list, index)
    #         inner_index -= 1



def _swap(list_, index):
    list_[index], list_[index - 1] = list_[index - 1], list_[index]


def _uniquify(list_):
    """Give unique identifier to items in list for stability testing."""
    return [(b, a) for a, b in enumerate(list_)]
