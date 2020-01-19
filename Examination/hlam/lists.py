s = [1, 2, 3, 4, 5, 6]
b = [11, 17, 19]
# s.extend(b) == s = s + b

print(s, b)
# s *= 5
# print(s.count(2))
# print(s.index(8))  ValueError
# s.pop(INDEX)
# s.remove(ELEMENT)
del s[1:6:2]
# a.sort() a = sorted(a, key=abs))

# s = "".join(a) Returns string


def x(value, lst=[]):
    lst.append(value)
    return lst


l1 = x('10')
l2 = x('20')

print(l1 is l2)

#  Розпакування списку:
# a, *rest = [1, 2, 3, 4, 5]  a = 1; b = [2, 3, 4, 5]

# COMPREHENTION
words = ['attribution', 'confabulation', 'elocution',
         'sequoia', 'tenacious', 'unidirectional']

vovels = sorted({''.join([l for l in word if l in 'aeiou']) for word in words})
print(vovels)
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
res = [(word, len(word)) for word in sent]
print(res)


