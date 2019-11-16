from collections import Counter

dct = {"one": 1, "two": 2, "three": 3}
# print(dct.get("two", 0))

with open('dob.txt', encoding="utf-8") as f:
    freq = dict(Counter(f.read().split()))
    common = Counter(f.read().split()).most_common(5)
print(common)