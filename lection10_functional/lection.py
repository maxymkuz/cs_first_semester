
names = ['Арман', 'Аркан', 'Аркана', 'Арсена', 'Пракс']


# def keys(name):
#     return name[-2]


# lst = sorted(names, key=keys)
lst = sorted(names, key=lambda name: name[-1])

print(lst)

elements = [(2, 12, 'Mg'), (1, 2, "Na"), (1, 3, "Li"), (1, 4, "Be")]
elements.sort(key=lambda e: (e[1], e[2]))
print(elements)
