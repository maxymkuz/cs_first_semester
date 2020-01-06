from copy import deepcopy


def make_board(n):
    """ int -> list
    Returns a list, filled with zeros, representing a board
    """
    column = [0 for i in range(n)]
    board = [column[:] for i in range(n)]
    return board


def print_result(n, lst_of_results):
    """ int, list -> None
    This function is used for printing all answers in an accessible way
    """
    print('_' * 20)
    for index, result in enumerate(lst_of_results):
        print(f'Solution №{index + 1}:')
        for row in result:
            print('0 ' * row + '1 ' + '0 ' * (n - row - 1))
        print('_' * 20)


def check_if_ok(board, row, column):
    """ list, int, int -> bool
    Returns True if we can place a queen on these coordinates, else False
    """
    # Checking the horizontal cells:
    for col in range(column):
        if board[row][col] == 1:
            return False
    row_down, row_up, col_diagonal = row, row, column

    # Cheching cells on the top left diagonal
    while row_up >= 0 and col_diagonal >= 0:
        if board[row_up][col_diagonal] == 1:
            return False
        col_diagonal -= 1
        row_up -= 1
    col_diagonal = column

    # Cheching cells on the bottom left diagonal
    while row_down < len(board) and col_diagonal >= 0:
        if board[row_down][col_diagonal] == 1:
            return False
        col_diagonal -= 1
        row_down += 1
    return True


def find_backtracking(n, board, lst_of_results, column=0):
    """ int, list, list, int -> bool
    Recursive algorithm that finds all possible solutions
    by backtracking to smaller boards
    """
    # When we reach the last column
    if column == n:
        return True

    for row in range(n):

        # Cheching if we can place a queen in this cell:
        if check_if_ok(board, row, column):
            # Placing a queen in this cell
            board[row][column] = 1

            # When we find a result, we save it to the lst_of_results and go on
            if column == n-1:
                if board not in lst_of_results:
                    lst_of_results.append(deepcopy(board))
                board[row][column] = 0
                continue

            # Going to the next column
            if find_backtracking(n, board, lst_of_results, column + 1):
                # When there's a solution for this column:
                return True

            # We can't place a queen here. There is no solution in next columns
            else:
                board[row][column] = 0
    return False


def convert_format(n, solutions):
    """ int, list -> None

    Converts the board states to a different format
    (e.g. [[0, 0, 1],[0, 1, 0],[1, 0, 0]] -> [0, 1, 2])
    """
    for index, solution in enumerate(solutions):
        result = [solution[row].index(1) for row in range(n)]
        solutions[index] = result


def duplicate_filter(n, solutions):
    """ int, list -> list

    Removes all of the duplicate solutions
    (mirror reflections, rotations, or both)
    """
    results = [solutions[0]]
    # First can't be duplicate, checking all others
    for solution in solutions[1:]:
        # Trying all different reflections/rotations
        mirror = solution[::-1]
        reverse = [n - 1 - row for row in mirror]
        miror_reverse = [n - 1 - row for row in solution]
        right_turn = [n - 1 - solution.index(i) for i in range(n)]
        left_turn = [solution.index(n - 1 - j) for j in range(n)]
        right_mirror = [n - 1 - mirror.index(k) for k in range(n)]
        left_mirror = [mirror.index(n - 1 - l) for l in range(n)]

        if mirror in results or reverse in results or miror_reverse in results:
            continue

        if right_turn in results or left_turn in results:
            continue

        if right_mirror in results or left_mirror in results:
            continue

        # If solution is not duplicate, we save it to results list
        results.append(solution)
    return results


def main():
    """ None -> None
    This function is used to call all other functions and print the result
    """
    # Inputting an n and checking if it's an integer >= 0
    while True:
        n = input("Enter the number of queens: ")
        if n.isdigit():
            n = int(n)
            break
        print("N has to be a positive integer!")

    if n < 4:
        if n == 0:
            print(f'\nTechnically, there are infinite solutions for n = {n}.')
        else:
            print(f'\nThere are no solutions for n = {n}.')
        return

    board = make_board(n)
    lst_of_results = []

    # Filling lst_of_results with all possible boards
    find_backtracking(n, board, lst_of_results)

    # Eliminate the duplicate solutions
    convert_format(n, lst_of_results)
    unique_results = duplicate_filter(n, lst_of_results)

    # Prinring the results
    print_result(n, unique_results)
    print(f'\nSolutions for n = {n}: {len(lst_of_results)}')
    print(f'Unique solutions for n = {n}: {len(unique_results)}\n')


if __name__ == "__main__":
    main()
