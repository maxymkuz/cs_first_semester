def make_board():
    """
    returns a list, representing 8*8 board
    """
    return [[0 for i in range(8)] for i in range(8)]


def print_board(board):
    """
    Prints a board
    """
    for i in board:
        for j in i:
            print(j, end=" ")
        print()


def convert_postition(pos):
    """
    str -> tuple
    returns a tuple with coordinates of a figure
    """
    second = int(pos[1]) - 1
    first = ord(pos[0]) - 97
    return first, second


def elephant(elephant_pos, board):
    """
    (tuple, list) -> list
    Returns a board with 1, where user cannot place
    a figure because elephant beats it
    """
    col = elephant_pos[0]
    row = elephant_pos[1]
    board[col][row] = 3
    # top left:
    i, j = col, row
    while i >= 0 and j >= 0:
        board[i][j] = 1
        i -= 1
        j -= 1
    i, j = col, row
    while i <= 7 and j >= 0:
        board[i][j] = 1
        i += 1
        j -= 1
    i, j = col, row
    while i <= 7 and j <= 7:
        board[i][j] = 1
        i += 1
        j += 1
    i, j = col, row
    while i >= 0 and j <= 7:
        board[i][j] = 1
        i -= 1
        j += 1


def turrel(pos, board):
    """
    tuple, list -> list
    writes 1 where turrel beats a cell
    """
    row = pos[0]
    col = pos[1]
    for i in range(len(board)):
        board[i][col] = 1
    for j in range(len(board)):
        board[row][j] = 1


def result(board):
    res = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                res.append([chr(i + 97), j + 1])
    return res


def main(elephant_pos, queen_pos):
    """
    (str, str) -> set
    Receives position of white elephant and queen
    and returns all possible positions for black figures
    """
    board = make_board()
    elephant_pos = convert_postition(elephant_pos)
    queen_pos = convert_postition(queen_pos)

    elephant(elephant_pos, board)
    turrel(queen_pos, board)
    elephant(queen_pos, board)

    res = result(board)
    for i in range(len(res)):
        res[i] = res[i][0] + str(res[i][1])
    set_res = set(res)
    return set_res


# print(main("b5", "g3"))
