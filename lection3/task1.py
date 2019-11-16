def hamming_weight(n):
    b = bin(n)[2:]
    print(n, b)
    counter = 0

    for c in b:
        if c == 1:
            counter += 1
    return(counter)


n = int(input())
#побітовий ссув
num = 5 ** n
# print(num, bin(num)[:2])

counter = hamming_weight(num)
if counter % 2 == 0:
    print("Number ", num," is evil number. Its hamming weight is ", counter,".")
if (counter % 2 == 1):
    print("Number ", num," is odious number. Its hamming weight is ", counter,".")






