main_lst = []

while True:
    try:
        num = int(input("Enter num of dishes: "))
        if num < 1:
            x = int("jasdhk")
        break
    except ValueError:
        print("enter integer >= 1")
        continue
for i in range(num):
    while True:
        try:
            name, price, weight = input(f"Enter dish №{i+1}: ").split()

            price = float(price)
            weight = float(weight)
            main_lst.append([name, price, weight])
            break
        except ValueError:
            print("enter integers >= 1")
            continue
main_lst.sort(key=lambda x: x[2]/x[1])
for dish in main_lst:
    print(dish[0], end=" ")
