def first():
    print(sum(map(int, bin(int(input()))[2:])))
    # OR
    res = bin(int(input()))[2:]
    counter = 0
    for c in res:
        counter += int(c)
    print( counter)


s = 'FF'
print(int(s, 16))#convert to decimal from 16,8,3



