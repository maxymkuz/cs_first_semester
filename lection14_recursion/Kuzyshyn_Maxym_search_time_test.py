import timeit


def while_loop(lst, find):
    i = 0
    while i != len(lst) and lst[i] != find:
        i += 1
    if lst[i] == find:
        return find
    return -1


def for_loop(lst, find):
    for i in range(len(lst)):
        if lst[i] == find:
            return find
    return -1


def sentinel_search(lst, find):
    length = len(lst)
    last_elem = lst[length - 1]
    lst[length - 1] = find
    i = 0
    while lst[i] != find:
        i += 1
    if i < length - 1 or last_elem == find:
        return find
    return -1


def index(lst, find):
    try:
        return lst.index(find)
    except ValueError:
        return -1


def avg(lst):
    return sum(lst) / len(lst)


def linear_time():
    SETUP_CODE = '''
from __main__ import while_loop, for_loop, sentinel_search, index, avg
from random import randint'''

    while_loop_code = '''
mylist = [x for x in range(10**5)]
find = randint(0, len(mylist))
while_loop(mylist, find)
    '''
    for_loop_code = '''
mylist = [x for x in range(10**5)]
find = randint(0, len(mylist))
for_loop(mylist, find)
    '''
    sentinel_code = '''
mylist = [x for x in range(10**5)]
find = randint(0, len(mylist))
sentinel_search(mylist, find)
    '''
    index_code = '''
mylist = [x for x in range(10**5)]
find = randint(0, len(mylist))
index(mylist, find)
    '''
    while_loop_time = timeit.repeat(setup=SETUP_CODE, stmt=while_loop_code,
                                    repeat=5, number=100)
    for_loop_time = timeit.repeat(setup=SETUP_CODE, stmt=for_loop_code,
                                  repeat=5, number=100)
    sentinel_time = timeit.repeat(setup=SETUP_CODE, stmt=sentinel_code,
                                  repeat=5, number=100)
    index_time = timeit.repeat(setup=SETUP_CODE, stmt=index_code,
                               repeat=5, number=100)
    f = open("search_time_test.txt", mode="w", encoding="utf-8")
    f.write(f"While loop search: {round(avg(while_loop_time), 3)}\n\
For loop time:{round(avg(for_loop_time), 3)}\nSentinel search: \
{round(avg(sentinel_time), 3)}\nIndex search: {round(avg(index_time), 3)}")


if __name__ == "__main__":
    linear_time()
