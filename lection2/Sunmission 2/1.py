try:
    x = int(input())
    y = int(input())
except:
    print("an error occured, please try again")

print("*" * y)
for i in range(x - 2):
    print("*" + " "*(y - 2) + "*")
print("*" * y)
