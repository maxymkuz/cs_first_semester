from functools import lru_cache

fibonacci = [1, 1]
i = 2
while len(fibonacci) < 1000:
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

    i += 1
# print(fibonacci)


def fib_recurtion_v2(n):
    if n == 0 or n == 1:
        return 1
    print(f"string is {n} totally cool")

    return fib_recurtion_v2(n-1) + fib_recurtion_v2(n-2)


cache = {0:1, 1:0}


def fib_3(n):
    if n-1 not in cache:
        cache[n - 1] = fib_3(n - 1)
    if n-2 not in cache:
        cache[n - 2] = fib_3(n - 2)
    return cache[n-1] + cache[n-2]


@lru_cache(maxsize=1000)
def fib_4(n):
    if n == 0 or n == 1:
        return 1
    return fib_4(n-1) + fib_4(n-2)


if __name__ == "__main__":
    print(fib_4(300))
