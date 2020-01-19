def quadratic(a, b, c):
    return lambda x: a*x**2 + b*x + c
# f = quadratic(2, 3, 5)
# print(f(1))


# res = list(map(lambda data: (data[0], data[-1]*9/5 + 32), temps)
# res = list(filter(lambda data: data > avg, data))
# res = list(filter(None, data))  -- to filter all empty elements