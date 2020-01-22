import functools
x = [4, 3, 6, 5, 8, 2, 7, 1, 11]
y = sorted(x)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 11]


def linear_search(lst, to_find):  # llst.index() If not--ValueError
    for i in range(len(lst)):
        if lst[i] == to_find:
            return i
    return False


def binary_search(lst, to_find):
    low = 0
    top = len(lst) - 1
    while top >= low:
        middle = (low + top)//2
        current = lst[middle]
        if current == to_find:
            return middle
        elif current > to_find:
            top = middle - 1
        else:
            low = middle + 1
    return -1


def main_rec_bin(lst, to_find):
    """
    Може не працювати для деяких випадків
    """
    def rec_binary_search(lst, to_find, low, top):

        if low > top:
            return -1
        middle = (low + top)//2
        current = lst[middle]
        if current == to_find:
            return middle
        elif current > to_find:
            return rec_binary_search(lst, to_find, low, middle-1)
        else:
            return rec_binary_search(lst, to_find, middle+1, top)
    return rec_binary_search(lst, to_find, 0, len(lst))


def rec_power(a, n):
    """
    raises a to the power n
    """
    if n == 0:
        return 1
    else:
        factor = rec_power(a, n//2)
        if n % 2 == 0:
            return factor * factor
        else:
            return factor * factor * a


def memorize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


# @functools.lru_cache(maxsize=None)
def fib_memorization(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        result = fib_memorization(n-1) + fib_memorization(n-2)
    return result


# fib_memorization = memorize(fib_memorization)


def selection_sort(lst):
    length = len(lst)
    for i in range(length):
        lowest_index = i
        for j in range(i + 1, length):
            if lst[j] < lst[lowest_index]:
                lowest_index = j
        lst[i], lst[lowest_index] = lst[lowest_index], lst[i]
    return lst


def insertion_with_insert_func(lst):

    def insert(lst, i):
        element = lst[i]
        print(element, i)
        for index in range(i):  # iterating in sorted part
            if index == i or element <= lst[index]:
                for j in range(i, index, -1):  # Shifting all elements left
                    lst[j] = lst[j - 1]
                lst[index] = element  # inserrting an element
                break

    for i in range(len(lst)):
        insert(lst, i)

    return lst


def insertion(lst):
    for i in range(len(lst)):
        element = lst[i]
        for index in range(i):  # iterating in sorted part
            if index == i or element <= lst[index]:  # We've found a place
                for j in range(i, index, -1):  # Shifting all elements left
                    lst[j] = lst[j - 1]
                lst[index] = element  # inserrting an element
                break
    return lst


def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]

        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]


def merge(lst1, lst2):
    """
    This function is used to merge two lists in a single,
    sorted list
    """
    res = []
    index1, index2 = 0, 0
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] <= lst2[index2]:
            res.append(lst1[index1])
            index1 += 1
        else:
            res.append(lst2[index2])
            index2 += 1
    res.extend(lst1[index1:])
    res.extend(lst2[index2:])
    return res


def merge_sort_rec(lst):
    if len(lst) <= 1:
        return lst
    index = len(lst)//2
    return merge(merge_sort_rec(lst[:index]), merge_sort_rec(lst[index:]))


def merge_without_rec(lst):
    temp = [[lst[i]] for i in range(len(lst))]
    i = 0
    while i < len(temp) - 1:
        temp.append(merge(temp[i], temp[i+1]))
        i += 2
    lst = temp[-1][:]
    return lst


def mergeSort_improved(a):

    def merge(a, start1, start2, end):
        index1 = start1
        index2 = start2
        length = end - start1
        aux = [None] * length
        for i in range(length):
            if ((index1 == start2) or
               ((index2 != end) and (a[index1] > a[index2]))):
                aux[i] = a[index2]
                index2 += 1
            else:
                aux[i] = a[index1]
                index1 += 1
        for i in range(start1, end):
            a[i] = aux[i - start1]

    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge(a, start1, start2, end)
        step *= 2


def quicksort_rec(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left = [elem for elem in lst if elem < pivot]
    right = [elem for elem in lst if elem > pivot]
    equal = [elem for elem in lst if elem == pivot]
    return quicksort_rec(left) + equal + quicksort_rec(right)


def quick_effective(lst):

    def sort_pivot(lst, pivot_index):
        pivot = lst[pivot_index]
        if pivot_index != -1:
            lst[pivot_index], lst[-1] = lst[-1], lst[pivot_index]

        j = len(lst) - 1
        i = 0

        while i != j:
            if lst[i] < pivot:
                i += 1
                continue
            elif lst[j] >= pivot:
                j -= 1
                continue
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
        lst[-1], lst[j] = lst[j], lst[-1]
        return j

    if len(lst) <= 1:
        return lst
    pivot_index = -1
    pivot = lst[pivot_index]
    if pivot_index != -1:
        lst[pivot_index], lst[-1] = lst[-1], lst[pivot_index]
    j = sort_pivot(lst, pivot_index)

    return quick_effective(lst[:j]) + [pivot] + quick_effective(lst[j+1:])


def quicksort_memory(array):
    """
    Алгоритм швидкого сортування без використання додаткової пам'яті.
    """
    def additional(array, start, stop):
        if stop - start > 0:
            pivot, left, right = array[start], start, stop
            while left <= right:
                while array[left] < pivot:
                    left += 1
                while array[right] > pivot:
                    right -= 1
                if left <= right:
                    array[left], array[right] = array[right], array[left]
                    left += 1
                    right -= 1
            additional(array, start, right)
            additional(array, left, stop)
    additional(array, 0, len(array) - 1)
    return array


RUN = 32


def insertionSort(arr, left, right):

    for i in range(left + 1, right+1):
        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


# merge function merges the sorted runs
def merge(arr, l, m, r):

    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m

    left = [arr[l + i] for i in range(len1)]
    right = [arr[m + 1 + i] for i in range(len2)]

    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    arr.extend(left[i:])
    arr.extend(right[:i])


# iterative tim_sort function to sort the
# array[0...n-1] (similar to merge sort)
def tim_sort(lst, n):

    # Sort individual subarrays of size RUN
    for i in range(0, n, RUN):
        insertionSort(lst, i, min((i+31), (n-1)))
    # start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = RUN
    while size < n:

        # pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2*size):

            # find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = left + size - 1
            right = min((left + 2*size - 1), (n-1))
            # merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            merge(lst, left, mid, right)

        size = 2*size
    return lst


print(tim_sort(x, len(x)))
