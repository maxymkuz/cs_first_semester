import math
n = int(input("Type Natural number: "))

i = 7

result = math.factorial(n)

while i <= n:
    result = int(result/i)
    i +=7

print(result)
