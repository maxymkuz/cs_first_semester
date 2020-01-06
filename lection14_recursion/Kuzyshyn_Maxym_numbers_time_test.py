import timeit
# import sys
# print(sys.getrecursionlimit())
m = -1


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


def fibonachi_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi_recursion(n-1) + fibonachi_recursion(n-2)


def fibonachi_recursion_depth(n):
    global m
    if m == -1:
        global top
        top = n
        m = 0
    depth = top - n
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fibonachi_recursion_depth(n-1) + fibonachi_recursion_depth(n-2)
    print(" "*depth, "fib(", n, " ) -->", res)
    return res


fibonachi_recursion_depth = memoize(fibonachi_recursion_depth)


# print(fibonachi_recursion_depth(30))


def fibonachi_iteration(n):
    fibonacci = [1, 1]
    if n < 2:
        return 1
    i = 2
    while len(fibonacci) < 1000:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        i += 1
    return fibonacci[n]


def factorial_iteration(n):
    x = 1
    for i in range(2, n+1):
        x *= i
    return i


def factorial_recursion(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


def numbers_time_test(func="fibonachi", realization="iteration", verbose=True):
    if func not in ["fibonachi", "factorial"]:
        string = "First argument has to be either 'fibonachi' or 'factorial'"
        print(string)
        return string
    if realization not in ["iteration", "recursion"]:
        string = "Second argument has to be either 'iteration' or 'recursion'"
        print(string)
        return string
    if func == "fibonachi" and realization == "iteration":
        f = "fibonachi_iteration"
    elif func == "fibonachi" and realization == "recursion":
        f = "fibonachi_recursion"

    setup = f'''from __main__ import {f}'''
    code = f'''{f}(35)'''
    time = timeit.repeat(setup=setup, stmt=code, number=100)
    print(time)
    # print(f(900))
    # print("Time is:", time.time() - time1)


numbers_time_test("fibonachi", "recursion", False)
