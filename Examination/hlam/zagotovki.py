import copy


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
