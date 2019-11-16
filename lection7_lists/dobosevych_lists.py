def my_key(x):
    return x[1]

lst = ["hey", "0", "1.18973560"]
lst1 = ["hey2", "02", "1.189735602", "234567", '34567890']

split_arr = list(zip(lst, lst1))
split_arr.sort(key=my_key)
# print(split_arr)

# lst.sort()
# print(lst[::-1])  # easy reverse
# print(" |  ".join(lst))


lst1 = ["hey2", "02", "03", "04", '05', "06", "bhlhgvjbh"]

# del lst1[2:6]
# lst1[2:6] = ["12345678"]
# lst1 *= 0  # clear or dublicate the sequence
# del lst1[1:6:2] 
print(lst1.pop(2))
print(lst1)
