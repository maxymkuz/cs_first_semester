def happy_number(num):
    """
    int -> bool
    Return True if ticket is happy and False otherwise
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """
    right_sum = 0
    left_sum = 0
    for i in range(4):
        right_sum += num % 10
        num //= 10
        
    for i in range(4):
        left_sum += num % 10
        num //= 10
    return right_sum == left_sum


def count_happy_numbers(n):
    """
    int-> int
    Returns a number of happy tickets in series from n tickets
    >>> count_happy_numbers(100000)
    714
    >>> count_happy_numbers(1000000)
    25926
    """
    res = 0
    for i in range(1, n + 1):
        if happy_number(i): res -= -1
    return res


def happy_numbers(m, n):
    """
    (int, int) -> list
    returns a number of happy tickets in range from m to n
    >>> happy_numbers(9999, 10500)
    [10001, 10010, 10100]
    >>> happy_numbers(156000, 160100)
    [156000, 160007, 160016, 160025, 160034, 160043, 160052, 160061, 160070]
    """
    res = []
    for i in range(m, n+1):
        if happy_number(i):
            res.append(i)
    return res
