import math
r = int(input("Radius: "))

volume = round(4 * math.pi * r**3 /3 , 3)
area = round(4 * math.pi * r**2 , 3)

print("V =" , volume )
print("A =" , area )