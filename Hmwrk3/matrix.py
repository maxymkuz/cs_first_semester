def saddle_point(matrix):
    """
    >>> saddle_point([[9, 8, 7], [5, 3, 2], [6, 6, 7]])
    [[2, 1]]
    >>> saddle_point([[3, 1, 3], [3, 2, 4]])
    [[1, 1], [1, 3]]
    >>> saddle_point([[1, 2, 3], [3, 1, 2], [2, 3, 1]])
    []
    """
    res = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            minimal = matrix[row][column]
            for i in range(len(matrix) - 1):
                minimal = min(matrix[i][column], matrix[i + 1][column])
            if matrix[row][column] == minimal == max(matrix[row]):
                res.append([row + 1, column + 1])
    return res


print(saddle_point([[2, 1, 4, 1]]))
