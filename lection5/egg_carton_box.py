def egg_carton_box(eggs): 
    """
    int -> list

    returns a list with integers, each of which represents number 
    of eggs in each box
    >>> egg_carton_box(12) # дві коробки по 6 яєць
    [6, 6]
    >>> egg_carton_box(28) # три коробки по 10 яєць. Варіант з двома коробками по 10 та двома по 4 відкидається бо це 4 коробки
    [10, 10, 10]
    >>> egg_carton_box(24) # дві коробки по 10 яєць та одна коробка на 4
    [4, 10, 10] 
    """   
    four_num = [1, 2, 3, 4, 13, 14, 23, 24]
    six_num = [5, 6, 11, 12, 15, 16, 21, 22, 25, 26]
    main = []
    while (eggs > 0):
        if eggs in four_num:
            main.append(4)
            eggs -= 4
        elif eggs in six_num:
            main.append(6)
            eggs -= 6
        else:
            main.append(10)
            eggs -= 10
    return sorted(main)
