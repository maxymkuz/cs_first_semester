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
    res = ""
    lst1 = [" " for i in range(8)]
    lst2 = [copy.copy(lst1) for i in range(8)]
    for i in crossword:
        lst2[i[1][0]][i[1][1]] = i[0]

    for i in range(8):
        for j in range(8):
            if lst2[i][j] == "":
                res += "  "
            else:
                res += lst2[i][j] + " "
        res += "\n"
    print(res)


if __name__ == "__main__":
    crossword = read_crossword('crossword_3_2.txt')
    print_crossword(crossword)
