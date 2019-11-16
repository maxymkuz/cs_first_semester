
def winning_combination(board):
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions if there is winning combination or False if not.

    >>> winning_combination([[0, 'g', 'g', 'g'], [0, 'g', 'w', 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 'g', 'g', 'g'], ['w', 'g', 'w', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 0], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'g', 'g', 'w'], [0, 0, 'w', 'g'], [0, 0, 'g', 'g'], [0, 0, 0, 'w'], ['w', 'g', 'g', 'g'], ['w', 'w', 'g', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 'g', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 'w', 'g']])
    False
    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], ['g', 'g', 'g', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'g'], [0, 0, 'w', 'w'], [0, 'w', 'w', 'g'], ['g', 'w', 'g', 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w']])
    False
    >>> winning_combination([[0, 'g', 'g', 'w'], [0, 0, 'w', 'g'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 'w', 'g', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], [0, 0, 0, 'w'], ['w', 'g', 'w', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], ['g', 'w', 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g']])
    (True, [[(3, 7), (3, 8), (3, 9), (3, 10)]])
    >>> winning_combination([[0, 'w', 'w', 'w'], [0, 0, 0, 'w'], [0, 'w', 'g', 'w'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'w', 'g'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], [0, 'g', 'w', 'g'], ['g', 'g', 'w', 'g'], ['w', 'g', 'w', 'g']])
    (True, [[(2, 13), (2, 14), (2, 15), (2, 0)], [(3, 5), (3, 6), (3, 7), (3, 8)], [(11, 3), (12, 2), (13, 1), (14, 0)], [(11, 3), (12, 2), (13, 1), (14, 0)], [(11, 3), (12, 2), (13, 1), (14, 0)]])
    >>> winning_combination([[0, 0, 'g', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 'w', 'g', 'g'], ['w', 'w', 'g', 'g'], ['w', 'g', 'g', 'w'], [0, 'g', 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 0, 0, 'g'], [0, 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'g', 'g']])
    (True, [[(3, 9), (3, 10), (3, 11), (3, 12)]])
    >>> winning_combination([[0, 0, 'w', 'w'], [0, 0, 'w', 'w'], ['g', 'g', 'g', 'w'], [0, 'w', 'g', 'g'], ['g', 'g', 'w', 'w'], [0, 0, 0, 'w'], [0, 0, 'w', 'w'], [0, 0, 'g', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 'w', 'w', 'w'], ['g', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 0], [0, 0, 'w', 'w']])
    (True, [[(3, 4), (3, 5), (3, 6), (3, 7)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> winning_combination([['g', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15), (3, 0), (3, 1)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    """
    res = []
    # Vertical
    for i in range(16):
        if board[i][0] == 0:
            continue
        if board[i][0] == board[i][1] == board[i][2] == board[i][3]:
            res.append([(0, i), (1, i), (2, i), (3, 1)])

    # Horizontal
    for row in range(4):
        for i in range(16):
            temp = [i, (i+1) % 16, (i+2) % 16, (i+3) % 16]

            if board[i][row] == 0:
                continue
            if board[i][row] == board[(i+1)%16][row] == board[temp[2]][row] == board[temp[2]][row] == board[temp[3]][row]:
                res.append([(row, i), (row, (i+1)%16), (row, (i+2)%16), (row, (i+3)%16)])

    # Diagonally 1
    for i in range(16):
        first = board[i][0]
        second = (i+1)%16
        third = (i+2)%16
        fourth = (i+3)%16
        if board[i][0] == 0:
            continue
        if board[i][0] == board[second][1] == board[third][2] == board[fourth][3]:
            res.append([(i, 0), (second, 1), (third, 2), (fourth, 3)])
    # Diagonally 2
        for i in range(16):
            first = board[i][0]
            second = (i+1)%16
            third = (i+2)%16
            fourth = (i+3)%16
            if board[i][3] == 0:
                continue
            if board[i][3] == board[second][2] == board[third][1] == board[fourth][0]:
                res.append([(i, 3), (second, 2), (third, 1), (fourth, 0)])

    if len(res) == 0:
        return False
    return True, res









import doctest
doctest.testmod()


print(winning_combination([[0, 0, 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], [0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 'w', 'w', 'w'], ['w', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], ['w', 0, 'g', 'g'], ['g', 'w', 'w', 'w'], [0, 0, 'w', 'w']]))