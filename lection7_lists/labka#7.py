def sieve_flavius0(n):
    odd_list = [i for i in range(1, n) if i % 2 == 1]
    third_list = []
    res = []
    for i, j in enumerate(odd_list):
        if ((i+1) % 3) != 0:
            third_list.append(j)
    for i, j in enumerate(third_list):
        if ((i+1) % 7) != 0:
            res.append(j)
    return res


print(sieve_flavius0(100))