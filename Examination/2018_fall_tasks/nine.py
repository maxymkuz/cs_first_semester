columns, rows = input("Enter a number of columns and rows: ").split()
columns = int(columns)
rows = int(rows)
number, index = 1, 0
line_of_integers = ""

while len(line_of_integers) < rows * columns:
    line_of_integers += str(number)
    number += 1

for row in range(rows):
    for col in range(columns):
        print(line_of_integers[index], end="")
        index += 1
    print()
