n = input()
number = 0
power = len(n)
for i in n:
    power -= 1
    number +=  int(i) * 2**power 

print(bin(number))
if n[0] == '0':
    print("0" + bin((number ^ (number>>1))).lstrip('-0b'))
else:
    print(bin((number ^ (number>>1))).lstrip('-0b'))


