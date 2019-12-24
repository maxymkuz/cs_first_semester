def make_board(n):
    column = [0 for i in range(n)]
    board = [column[:] for i in range(n)]
    return board


def print_board(board):
    print("_______________________")
    for row in range(len(board)):
        for column in range(len(board)):
            print(board[row][column], end=" ")
        print()


def find_backtracking(n, board, column=0):

    if column == n:
        print("reached the end")
        return True

    for row in range(n):
        correct_choice = True
        print("               ", row, column, board[row][column])

        for c in range(column):
            if board[row][c] == 1:
                print("Falseure", row, c, column)
                correct_choice = False

        print_board(board)

        if correct_choice:
            board[row][column] = 1
            is_possible = find_backtracking(n, board, column+1)

            print("Possible: ", is_possible)


    # print(find_backtracking(n, board, column+1))
    return True


n = 3
board = make_board(n)
find_backtracking(n, board)
