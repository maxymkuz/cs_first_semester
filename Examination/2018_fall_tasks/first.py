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
            num = int(input("Enter num of rows: "))
            if num < 1:
                x = int("jasdhk")
            lst_with_length.append(num)
            break
        except ValueError:
            print("enter integer >= 1")
            continue

for i in range(len(lst_with_length)):
    print("*"*lst_with_length[i])
