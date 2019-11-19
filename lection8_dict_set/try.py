import copy

def calculate(number):
    """
    function calculates number of elements, the highest and the lowest, their sum, average and median
    >>> calculate([1, 2, 3, 4, 5])
    ([1, 2, 3, 4, 5], 5, 15, 1, 5, 3.0, 3)
    >>> calculate([2, 4, 6, 7, 3])
    ([2, 4, 6, 7, 3], 5, 22, 2, 7, 4.4, 4)
    >>> calculate([5, 7, 3, 6, 3])
    ([5, 7, 3, 6, 3], 5, 24, 3, 7, 4.8, 5)
    """
    cp = copy.copy(number)
    count = len(number)
    sum = 0
    for j in number:
        # j=int(j)
        sum += j
    number1 = sorted(number)
    highest = number1[len(number1)-1]
    lowest = number1[0]
    mean = sum/len(number)
    if count % 2 == 1:
        median = number1[int(count/2)]  
    else:
        median = (number1[int(count/2)] + number1[int(count/2 - 1)])/2
    return cp, count, sum, lowest, highest, mean, median

# ([5, 4, 1, 8, 5, 2], 6, 25, 1, 8, 4.166666666666667, 4.5)
print(calculate([5,4,1,8,5,2]))
import doctest
doctest.testmod()