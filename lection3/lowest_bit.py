def lowest(num:int):
    lowest_bit_position = 0
    while True:
        #print(bin(num))
        #Checking if the last bit in num is equal to 1
        if num & 1:
            break
        #deleting the last bit, that's equal to 0
        num = num >> 1
        lowest_bit_position += 1
    return(lowest_bit_position)


n = int(input("enter integer:"))
#lowest(n)-- is our position
print(lowest(n))