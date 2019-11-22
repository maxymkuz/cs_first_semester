import copy


def read_crossword(path):
    """
    str -> list
    Return list of tuples with crossword letters and it's positions
    >>> read_crossword('crossword_3_2.txt')
    [('o', (0, 1)), ('o', (3, 1)), ('o', (5, 1)), ('o', (4, 3)),...
    """
    res = []
    temp = ()

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            line = line.split(" ")
            if len(line[0]) < 3:
                letter = line[0][0]
            else:
                for i in line:
                    temp = (letter, (int(i[1]), int(i[3])))
                    res.append(temp)
    return res


def print_crossword(crossword):
    """ list -> str

    Print crossword
    """
    max_col = -1
    max_row = -1
    for x in crossword:
        col = x[1][0]
        row = x[1][1]
        if row > max_row:
            max_row = row
        if col > max_col:
            max_col = col

    lst1 = [" " for i in range(max_row + 1)]
    lst2 = [copy.copy(lst1) for i in range(max_col + 1)]

    for i in crossword:
        lst2[i[1][0]][i[1][1]] = i[0]

    for i in range(max_row + 1):
        res = ''
        for j in range(max_col + 1):
            if lst2[i][j] == "":
                res += " "
            else:
                res += lst2[i][j]
        
        res = res.split(" ")
        for word in res:
            if len(word) > 1:
                print(word)

    for j in range(max_col + 1):
        res = ''
        for i in range(max_row + 1):
            if lst2[i][j] == "":
                res += " "
            else:
                res += lst2[i][j]
        res = res.split(" ")
        for word in res:
            if len(word) > 1:
                print(word)

    res = ''
    for i in range(max_row + 1):
        for j in range(max_col + 1):
            if lst2[i][j] == "":
                res += " "
            else:
                res += lst2[i][j] + " "
        res += "\n"
    



if __name__ == "__main__":
    crossword = read_crossword('crossword_3_2.txt')
    print_crossword(crossword)
