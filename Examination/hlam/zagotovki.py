import copy
import random
import sys


# string = "87.65.4321"
def first(string):
    result = ""
    while len(string) > 1:
        result += string[3:5] + "/"
        string = string[1:-1:2]
    print(result, string)


def tzilotchyselno(x, y):
    print((y % 10)**3)
    print((x//10) % ((y % 10)**3), end='|')
    if x < y:
        return isinstance(x/10, type(x))


a = [12, 54, 62]
b = copy.copy(a)
# print(a[-1] is b[-1])

# a, b, c = list(range(1, 10))[1::3]

# <<<<< LAMBDA MAP FILTER >>>>>
x = [12, 34]
# print(' '.join(list(map(int, x))))
# x = abcd
# print(list(map(list, x)))
# print(list(map(list, ['ab', 'cd'])))
# random.randint(4, 10)
# print(sys.getsizeof('abc'))


def ct3(a):
    l, m, n = [], [], len(a)
    for val in a[n-1:0:-2]:
        l.append(val % 10)
        m += [int(str(val)[0])]
        if sum(m) > 3:
            l.append(m.pop(0))
    returt l + m