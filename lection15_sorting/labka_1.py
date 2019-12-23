import copy


def read(path):
    """
    string -> list
    Returns a list with tuples of names and number
    """
    lst = []
    f = open(path, "r")
    first_line = True
    for line in f:
        if first_line:
            first_line = False
            continue
        line = line.strip().split()
        num = int(line[1][1:-1])
        lst.append((line[0], num))
    f.close()
    return lst


lst = read("girls_name.txt")


def filter(lst):
    """
    lst -> lst
    returns a list of all names that only one children has
    """
    res = []
    for name in lst:
        if name[1] == 1:
            res.append(name[0])
    return res


def buble_sort(lst):
    """
    lst -> lst
    Sorting the list by second elem in each elem using buble sort and returning
    this list
    """
    lst_sorted = copy.copy(lst)
    for i in range(len(lst_sorted)):
        for j in range(len(lst_sorted)):
            if j == len(lst_sorted) - 1:
                continue
            if lst_sorted[j][1] > lst_sorted[j + 1][1]:
                lst_sorted[j], lst_sorted[j+1] = lst_sorted[j+1], lst_sorted[j]
    
    return lst_sorted


lst_sorted = buble_sort(lst)


def most_popular_binary(lst_sorted):
    """
    print 10 most popular names
    """
    for l in range(1, 11):
        print(l, lst_sorted[-l])


def binary_ones(lst_sorted):
    """
    searching all names that happened only once
    """
    i = 0
    res = []
    while lst_sorted[i][1] == 1:
        res.append(lst_sorted[i])
        i += 1
    return res


def most_popular(lst):
    """
    lst -> string
    returns a name that is most frequent 
    """
    lst2 = copy.copy(lst)
    most_pop = []

    for j in range(10):
        biggest = 0
        biggest_name = ""
        index = 0
        for i in range(len(lst2)):
            if lst2[i][1] > biggest:
                biggest = lst2[i][1]
                biggest_name = lst2[i][0]
                index = i
        most_pop.append((j+1, biggest, biggest_name))
        del lst2[index]   
    return most_pop



def letter_name(lst, letter):
    """
    lst, string -> tuple
    returns a letter taht most names start with, num of names starting with it
    arr of names and sum of children
    """
    arr = [0 for i in range(100)]
    counter = 0
    for name in lst:
        letter = name[0][0].lower()
        order = ord(letter) - 1072
        arr[order] += 1
    maximum = 0
    letter = ""
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
            letter = chr(i + 1072)
    arr_of_names = []
    sum_of_children = 0
    for name in lst:
        if name[0][0].lower() == letter:
            arr_of_names.append(name[0])
            sum_of_children += name[1]
    return letter, maximum, arr_of_names, sum_of_children


# print(letter_name(lst, "a"))


def merge_two(l, r):
    """
    Functon used for merge sort
    """
    new = []
    i1, i2 = 0, 0
    while i1 != len(l) and i2 != len(r):
        if l[i1] < r[i2]:
            new.append(l[i1])
            i1 += 1
        else:
            new.append(r[i2])
            i2 += 1
    # print(new, i1, i2, "______")

    new.extend(l[i1:])
    new.extend(r[i2:])
    return new


def merge_sort(lst):
    num = lst[1]
    if len(lst) > 1:
        middle = int(len(lst)/2)
        left = lst[:middle]
        right = lst[middle:]

        left = merge_sort(left)
        right = merge_sort(right)
        x = merge_two(left, right)
        return x
    return lst