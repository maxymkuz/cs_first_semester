def quicksort(lst):
    if not lst:
        return []
    left = []
    right = []
    point = lst[-1]
    for i in range(len(lst)):
        if lst[i] > point:
            right.append(lst[i])
        else:
            left.append(lst[i])
    res = quicksort(left) + quicksort(rigth)
    return res


print(quicksort([1, 3, 5]))
