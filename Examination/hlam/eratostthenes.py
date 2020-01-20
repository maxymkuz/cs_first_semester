import math
from itertools import combinations


def primes(n):
    lst = [1 for i in range(n+1)]
    root = math.ceil(math.sqrt(n))
    for i in range(2, root):
        if lst[i] == 1:
            for j in range(i*2, n+1, i):
                lst[j] = 0
    for i in range(len(lst)):
        if lst[i] == 1:
            lst[i] = i
    return list(filter(lambda x: x > 0, lst))


x = primes(1000000)

print(x[10000])


def digits(number):
    str_num = str(number)
    num_digits = len(str_num)
    for replaced in range(1, num_digits):
        indexes = list(combinations([i for i in range(num_digits)], replaced))

        for comb in indexes:
            res = 0
            T = ""
            sample = ""
            for i in range(num_digits):
                if i in comb:
                    T += '0'
                    sample += '1'
                else:
                    sample += '0'
                    T += str_num[i]
            T = int(T)
            sample = int(sample)
            # print(number, comb, T, sample)
            for num in range(10):
                if num == 3 and res == 0:
                    break
                if num == 4 and res <= 1:
                    break
                if num == 6 and res <= 3:
                    break

                if T in x:
                    res += 1

                T += sample

            if res >= 7:
                print(number, comb, res)


for prime in range(0, 11450):
    digits(x[prime])
