def func(n):
    return lambda a: a * n

b = func(3)(12)
c = func(3)(11)
print(func(2)(4))
print("c > b") if c > b else print("c < b")

