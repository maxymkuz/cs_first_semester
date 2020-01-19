a = b = 55
xbin = 0b111  # == bin(777)
# help(len)


def func(x, arg=[]):
    arg.append(x)
    return arg


# print(dir())

x = 100


def first(y):
    global x
    x += y
    return y + x


vars()

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(enumerate(seasons, start=2)))


# try:
#     month = int(input("enter: "))
#     assert(1 <= month <= 12)  # It's like we throw an error
# except AssertionError:
#     print("Got here")
