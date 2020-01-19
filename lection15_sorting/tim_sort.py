from random import randint
MINRUN = 32
lst = [12, 7, 17, 9, 11, 220, 1, 3, 4, 11, 5, 1000]


def binary_index_search(lst, num, end=0, start=0):
    middle = (start + end) // 2
    if lst[middle] < num:
        if middle + 1 == end:
            return middle + 1

        if lst[middle + 1] > num:
            return middle + 1
        start = middle

        return find_insert(lst, num, end, start)
    elif lst[middle] > num:
        if middle == start:
            return start
        if lst[middle - 1] < num:
            return middle
        end = middle

        return find_insert(lst, num, end, start)
    else:
        return middle


def binary_insertion(lst, start, end):
    for i in range(start + 1, end + 1):
        num = lst[i]

        index_to_append = find_insert(lst, num, i)
        for j in range(i, index_to_append, -1):
            lst[j] = lst[j - 1]

        lst[index_to_append] = num
    return lst


lst = [randint(0, 10) for i in range(64)]
print(binary_insertion(lst, 0))


def merge(arr, left, middle, right):

    # original array is broken in two parts
    # left and right array
    len1, len2 = middle - left + 1, right - middle
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[left + i])
    for i in range(0, len2):
        right.append(arr[middle + 1 + i])

    index1, index2, index = 0, 0, left
    # after comparing, we merge those two array
    # in larger sub array
    while index1 < len1 and index2 < len2:

        if left[index1] <= right[index2]:
            arr[index] = left[index1]
            index1 += 1
        else:
            arr[index] = right[index2]
            index2 += 1
        index += 1

    # copy remaining elements of left, if any
    while index1 < len1:
        arr[index] = left[index1]
        index += 1
        index1 += 1

    # copy remaining element of right, if any
    while index2 < len2:
        arr[index] = right[index2]
        index += 1
        index2 += 1
