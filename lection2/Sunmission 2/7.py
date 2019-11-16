#try:
x = input()
n = int(x)
if n >= 2:
    prime = True

    if int(x[len(x) - 1]) % 2 != 0:
        print(2)
    else:
        for i in range(1, n, 2):
            prime = True
            for j in range(3 , i):
                if i % j == 0:
                    prime = False
            if prime: 
                if n % i != 0:  
                    print(i)
                    break
#     else: 
#         print(0/0)
# except:
#     print("Error")


