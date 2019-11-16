from random import randint


def add_to_stick(res, stick, is_green):
    is_added = False
    for j in range(3, -1, -1):
        if res[stick][j] == 0:
            is_added = True
            if is_green:
                res[stick][j] = "g"
                is_green = False
                break
            else:
                is_green = True
                res[stick][j] = "w" 
                break
    return res, is_green


def board_generation():
    """
    () -> list

    Generates a game board of 16 x 4 size, i.e. two dimensional list (array) of 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

    """
    res = []
    is_green = True

    for i in range(16):
        res.append([0, 0, 0, 0])
    x = randint(14, 16)
    for i in range(x):
        stick = randint(0, 15)
        res, is_green = add_to_stick(res, stick, is_green)
    return res

board_generation()