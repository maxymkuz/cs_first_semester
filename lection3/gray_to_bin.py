n = input()
res = ""

res += n[0]
print(n)

for i in range(1, len(n)):
    print(res, i)
    if (n[i] == '0'): 
        res += res[i - 1];  
    else: 
        if (res[i - 1] == '1'):
             res += "0" 
        if (res[i - 1] == '0'):
             res += "1"

print(res)

