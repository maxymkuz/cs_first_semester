x = int(input())
lst = []
res = 0
while True:
    if x == 0:
        break
    lst.append(x%10)
    x //= 10
for i in range(int(len(lst)/2) + 1):
    if lst[i] == lst[len(lst) - i -1]:
        res += 1
print(res)
