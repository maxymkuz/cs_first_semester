def hamming_dist(a,b):
    ones = 0
    subject = x^y

    for char in range(len(bin(subject)[2:])):
        if bin(subject)[len(bin(subject)) - 1] > bin((subject>>1)<<1)[len(bin(subject)) - 1]:
            ones+=1
        subject = subject>>1

    return ones

x,y = input('Enter two values: ').split()
x = int(x)
y = int(y)

print(hamming_dist(x,y))