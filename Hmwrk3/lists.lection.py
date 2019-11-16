# msg = ''
# for s in "secret".split("e"):

#     msg = msg + s
# print(msg)
# def f1(str1):
#     res = ""
#     while(len(str1) > 1):
#         res += str1[3:5] + "|"
#         str1 = str1[1:-1:2]
#     print(res)

# f1("87.65.4321")
import copy
# def first(a):
#     one = a
#     two = copy.copy(a)
#     three = copy.deepcopy(a)
#     two[0] = 1
#     three[1] = 2
#     one[2] = a[0]
#     print("two:", str(two) + str(three))

# first([10,5,8,3])


# def first(lst1):
#     res = []
#     lst2 = copy.copy(lst1)
#     if lst1 == lst2:
#         res.append('1')
#     lst2.pop(2)
#     if lst1 is lst2:
#         res.append('2')
#     if lst1[-1] == lst2[-1]:
#         res.append('3')
#     print(res)
# first([12,54,62])