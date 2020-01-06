def insert(lst, i, num_of_sorted):
    element = lst[i]
    for index in range(num_of_sorted):
        if index == num_of_sorted or element <= lst[index]:
            for j in range(i, index, -1):
                lst[j] = lst[j - 1]
            lst[index] = element
            break
    print(lst)
    return lst


def insertion(lst):
    num_of_sorted = 0
    for i in range(len(lst)):
        lst = insert(lst, i, num_of_sorted)
        num_of_sorted += 1
    return lst


import random

lst = [random.randint(-10000, 10000)/1000 for x in range(100)]
print(insertion(lst))
