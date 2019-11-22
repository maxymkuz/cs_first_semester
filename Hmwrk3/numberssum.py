def numbers_sum(n):
    """
    int -> int
    returnd a sum of n elems
    >>> numbers_sum(5)
    25
    >>> numbers_sum(1)
    3
    """
    nar = [1, 1, 1]
    luc = [2, 1, 3]
    if n < 1:
        return 0
    if n == 1:
        return 3
    if n == 2:
        return 5
    for i in range(3, n + 1):
        nar.append(nar[i-1] + nar[i-3])
        luc.append(luc[i-1] + luc[i-2])
    return sum(nar) + sum(luc)

print(numbers_sum(1))