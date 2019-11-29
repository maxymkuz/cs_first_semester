def lgen(even=False, nmax=1000000):
    """
    happy numbers with generator using
    """
    start = 2 if even else 1
    n, lst = 1, list(range(start, nmax + 1, 2))  # List full of odd numbers 
    len_lst = len(lst)
    yield lst[0]

    print(lst)
     
    while n < len_lst and lst[n] <= len_lst:
        yield lst[n]
        print(lst[n], "it's oouuuut")
        n += 1
        lst = [j for i, j in enumerate(lst, 1) if i % lst[n]]
        print(lst)
        len_lst = len(lst)

    print(lst)
    for i in lst[n:]:
        print('third')
        yield i


# for i in lgen(nmax=10):
#     print(i)

vuraz_generator = (x for i in [1, 65, 53, 11])
print(vuraz_generator)
