# a, b = input()
# print(a, b)
# a = b = c = d = 20 #every variable will be equal to 20

# try:
#     print(int("jbtrk"))
# except ValueError as err:
#     print(err)


def is_normal(n :int, b :int) -> bool:
    return(n % b == 0)

print(is_normal(56, 67))

