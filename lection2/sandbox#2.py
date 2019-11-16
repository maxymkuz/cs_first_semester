# x = int(input())
# y = int(input())
# for i in range(x):
#     print(y*"*")

# x = 45.6
# y = 2
# thing = divmod(x, y)
# print(thing)

import math
a,b,c = eval(input())
# a = float(a)
# b = float(b)
# c = float(c)
print(type(a))
D = math.sqrt(b**2 - 4*a*c)
root1 = (-b + D)/2*a
root2 = (-b - D)/2*a


print(root1, "  ", root2)