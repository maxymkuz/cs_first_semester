import copy


def flatten(lst: list, first_iter=True):
    """
    Returns the values of lists in lists
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
    if not isinstance(lst, list):
        return lst
    mamka = copy.copy(lst)
    for i in range(len(mamka)):
        if isinstance(mamka[i], list):
            mamka[:i + 1] = mamka[:i] + flatten(mamka[i], first_iter=False)
    return mamka


lst = [1, 2, [3, [4, [5.1, 5.2]], 6], 7]
print(flatten(lst))
print(lst)
