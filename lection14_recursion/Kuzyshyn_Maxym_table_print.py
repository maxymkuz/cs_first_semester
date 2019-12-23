while True:
    try:
        columns = int(input("Enter number of columns: "))
        rows = int(input("Enter number of columns"))
        break
    except ValueError:
        print("you need to enter 2 integers by 'enter'")
arr = [["     "]*rows for i in range(columns)]


def calculate_row_column(i, j):
    if j == 0 or i == 0:
        digit = 1
        return 1
    return calculate_row_column(i-1, j) + calculate_row_column(i, j-1)


for i in range(columns):
    for j in range(rows):

        number = str(calculate_row_column(i, j))
        arr[i][j] = arr[i][j][:5-len(number)] + number
        print(arr[i][j], end="")
    print("\n")
