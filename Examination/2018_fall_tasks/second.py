while True:
    try:
        num = int(input("Enter num of rows: "))
        if num < 1:
            x = int("jasdhk")
        break
    except ValueError:
        print("enter integer >= 1")
        continue

lst_with_length = []

for i in range(num):
    while True:
        try:
            num = int(input("Enter temperatures:"))
            lst_with_length.append(num)
            break
        except ValueError:
            print("enter integer >= 1")
            continue

length = len(lst_with_length)
lst_with_length = list(filter(lambda x: x > 0, lst_with_length))
print(lst_with_length)
print("LENGTHJN:", length, len(lst_with_length))

print(sum(lst_with_length)/len(lst_with_length), min(lst_with_length),
      max(lst_with_length), (length - len(lst_with_length))/length)
