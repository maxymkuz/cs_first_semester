power = int(input())
num = 5**power
x = num
counter = 0

while num > 0:
    if num & 1 == 1:
        counter += 1
    num = num >> 1

if counter % 2 == 0:
    print("Number", x, "is evil number. Its hamming weight is", str(counter) + ".")

if counter % 2 == 1:
    print("Number", x, "is odious number. Its hamming weight is", str(counter) + ".")
