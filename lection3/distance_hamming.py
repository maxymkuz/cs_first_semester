x, y = (input("Enter two values: ").split())
x, y = int(x), int(y)
xory = x ^ y

counter = 0
for i in range(len(bin(xory))):
    if (xory >> i) & 1:
        counter += 1

print(counter)






