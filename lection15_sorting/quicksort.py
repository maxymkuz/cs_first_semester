from random import randint
from time import time
import timeit


def avg(lst):
    return sum(lst) / len(lst)


def quicksort_first(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left = []
    right = []
    equal = [pivot]
    for i in range(len(lst) - 1):
        if lst[i] < pivot:
            left.append(lst[i])
        elif lst[i] > pivot:
            right.append(lst[i])
        else:
            equal.append(lst[i])

    return quicksort_first(left) + equal + quicksort_first(right)


def quicksort_simple_advanced(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    left = [elem for elem in lst if elem < pivot]
    right = [elem for elem in lst if elem > pivot]
    equal = [elem for elem in lst if elem == pivot]
    return quicksort_simple_advanced(left) + equal + quicksort_simple_advanced(right)


def find_pivot(lst):
    a, b, c = 0, len(lst) // 2, -1
    if lst[a] != max([lst[a], lst[b], lst[c]]):
        if lst[a] != min([lst[a], lst[b], lst[c]]):
            return a
        return b if lst[b] <= lst[c] else c
    return b if lst[b] >= lst[c] else c


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


def quicksort_effective(lst):
    if len(lst) <= 1:
        return lst
    # pivot_index = find_pivot(lst)
    pivot_index = -1
    pivot = lst[pivot_index]
    if pivot_index != -1:
        lst[pivot_index], lst[-1] = lst[-1], lst[pivot_index]
    j = sort_pivot(lst, pivot_index)

    return quicksort_effective(lst[:j]) + [pivot] + quicksort_effective(lst[j+1:])


def merge_two(l, r):
    new = []
    i1, i2 = 0, 0
    while i1 != len(l) and i2 != len(r):
        if l[i1] < r[i2]:
            new.append(l[i1])
            i1 += 1
        else:
            new.append(r[i2])
            i2 += 1

    new.extend(l[i1:])
    new.extend(r[i2:])
    return new


def merge_sort(lst):
    if len(lst) > 1:
        middle = int(len(lst)/2)
        left = lst[:middle]
        right = lst[middle:]

        left = merge_sort(left)
        right = merge_sort(right)
        x = merge_two(left, right)
        return x

    return lst


def buble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than or 
        # equal to pivot 
        if   arr[j] <= pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# Driver code to test above 


SETUP_CODE = '''
from __main__ import buble_sort, merge_sort, quicksort_first, merge_two,\
 sort_pivot, quicksort_simple_advanced, avg, partition, quickSort
from random import randint'''

merge_sort_code = '''
mylist = [randint(0, 10**4) for x in range(10**5)]
merge_sort(mylist)
    '''
quicksort_first_code = '''
mylist = [randint(0, 10**4) for x in range(10**5)]

quicksort_first(mylist)
    '''
quickSort = '''
arr = [randint(0, 10**4) for x in range(10**5)]
n = len(arr)
quickSort(arr,0,n-1)
    '''

merge_time = timeit.repeat(setup=SETUP_CODE, stmt=merge_sort_code,
                           repeat=2, number=5)
quicksort1_time = timeit.repeat(setup=SETUP_CODE, stmt=quicksort_first_code,
                                repeat=2, number=5)
quicksort2_time = timeit.repeat(setup=SETUP_CODE, stmt=quickSort,
                                repeat=2, number=5)
f = open("search_time_test.txt", mode="w", encoding="utf-8")
f.write(f"merge time:{round(avg(merge_time), 3)}\nQuick complicated: \
{round(avg(quicksort1_time), 3)}\nQuick easy: {round(avg(quicksort2_time), 3)}")
