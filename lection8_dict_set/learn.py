file = open("dob.txt", "r", encoding="utf-8")
lines = file.readlines()
# print(lines)
# for line in file:
#     print(line + '\n')
# print(f + '\n')

a = 2
b = a
a = 12
print(id(a))
print(id(b))

