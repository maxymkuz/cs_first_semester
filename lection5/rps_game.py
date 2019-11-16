def rps_game(lst):
    """
    list -> list
    """

    tpl = []
    for i in lst:
        i = i.upper()
        if i[0] == i[1]:
            tpl.append((False, False))
        elif i[0] == "S" and i[1] == "P":
            tpl.append((True, False))
        elif i[0] == "P" and i[1] == "S":
            tpl.append((False, True))
        elif ord(i[0]) < ord(i[1]):
            tpl.append((True, False))
        else:
            tpl.append((False, True))


    return tpl

print(ord('S'), ord('R'), ord('P'))

print(rps_game(['SS', 'RS', 'PS']))


