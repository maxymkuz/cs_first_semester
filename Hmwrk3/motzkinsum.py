def motzkin_sum(n):
    """
    int -> int
    returns n-th number in motskin sequence
    >>> motzkin_sum(10)
    232
    >>> motzkin_sum(5)
    3
    >>> motzkin_sum(1)
    1
    """
    motskin = [0]*(n + 2)
    motskin[0] = 1
    motskin[1] = 0
    for i in range(2, n+2):
        motskin[i] = (i-1)*(2*motskin[i-1] + 3*motskin[i-2])/(i+1)
    return int(motskin[n - 1])


print(motzkin_sum(1))
