s = int(input())
num = 5**s
print(num)
print(bin(num))



for i in range(8):
    print (num >> i & 1)
