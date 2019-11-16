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
    lst1 = [" " for i in range(10)]
    lst2 = [lst1 for i in range(10)]
    print(lst2)
    res = ""
    for i in crossword:
        letter = i[0]
        tpl = i[1]
        print(letter, tpl[0], tpl[1])
        lst2[tpl[0]][tpl[1]] = letter
    for i in len(lst2):
        
    print(lst2)



if __name__ == "__main__":
    crossword = read_crossword('crossword_3_2.txt')
    print_crossword(crossword)
