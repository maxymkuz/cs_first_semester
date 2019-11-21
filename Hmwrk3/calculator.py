import copy


def calculate(numbers):
    """
    list -> tuple
    returns biggest/lowest/average/number element in list
    >>> calculate([2, 4, 6, 7, 3])
    ([2, 4, 6, 7, 3], 5, 22, 2, 7, 4.4, 4)
    >>> calculate([5, 7, 3, 6, 3])
    ([5, 7, 3, 6, 3], 5, 24, 3, 7, 4.8, 5)
    """
    cp = copy.copy(numbers)
    x = len(numbers)
    for j in range(len(numbers)):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    count = len(numbers)
    summary = sum(numbers)
    lowest = min(numbers)
    highest = max(numbers)
    avg = summary/x
    if x % 2 == 1:
        median = numbers[int(x/2)]  
    else:
        median = (numbers[int(x/2)] + numbers[int(x/2 - 1)])/2
    return (cp, count, summary, lowest, highest, avg, median)

print(calculate([5, 4, 1, 8, 5, 2]))
# if __name__ == "__main__":
#     num_arr = []
#     while True:
#         elem = input()
#         if elem == '':
#             break
#         try:
#             num_arr.append(int(elem))
#         except:
#             print("Error")
#     numbers, count, summary, lowest, highest, avg, median = calculate(num_arr)

#     print(f'numbers: {str(numbers)}')
#     print(f'count = {str(count)} sum = {str(summary)} lower = {str(lowest)} heighest = {str(highest)} mean = {str(avg)}')
