import math


def primes(n):
    lst = [1 for i in range(n+1)]
    root = math.ceil(math.sqrt(n))
    for i in range(2, root):
        if lst[i] == 1:
            for j in range(i*2, n+1, i):
                lst[j] = 0
            print(lst)
    for i in range(len(lst)):
        if lst[i] == 1:
            lst[i] = i
    print(lst)


primes(20)