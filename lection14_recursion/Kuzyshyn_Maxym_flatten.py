import copy


def has_no_list(lst):
    """
    list -> bool
    Returns true if there aren't any list inside lst
    """
    for element in lst:
        if isinstance(element, list):
            return False
    return True


def flatten(lst, first_iter=True):
    """
    Returns the values of lists in given list
    >>> flatten([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten([[]])
    []
    >>> flatten(3)
    3
    >>> flatten([1,[2]])
    [1, 2]
    >>> flatten([])
    []
    """
    if first_iter:
        lst = copy.deepcopy(lst)
    if not isinstance(lst, list) or has_no_list(lst):
        return lst
    i = 0
    while i < len(lst):
        counter = 0
        if isinstance(lst[i + counter], list):
            if not has_no_list(lst[i + counter]):
                lst[i + counter] = flatten(lst[i + counter], False)
            for subelem in lst[i]:
                lst.insert(i + counter, subelem)
                counter += 1
            del lst[i + counter]
        i += 1
    return lst


lst = [1, 2, [3, [4, [5.1, 5.2]], 6], 7]
print(flatten(lst))
print(lst)
