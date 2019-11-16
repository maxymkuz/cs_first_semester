import math
print(math.pi)

def leibniz_gregory_adhava(n):
    num = 0
    num_of_elements = 10**n
    for i in range(1, num_of_elements, 4):
        num += 4/i
    for j in range(3, num_of_elements, 4):
        num -= 4/j
    print(int(num_of_elements/2))
    print("Difference is: ", abs(math.pi - num))
    print(num)









n = int(input("insert n(1 <= n <= 8) Leibniz-Gregory-Madhava: "))
leibniz_gregory_adhava(n)