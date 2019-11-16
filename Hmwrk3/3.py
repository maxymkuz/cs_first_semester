import copy


def calculate(numbers):
    """
    list ->
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


if __name__ == "__main__":
    num_arr = []
    while True:
        elem = input()
        if elem == '':
            break
        try:
            num_arr.append(int(elem))
        except:
            print("Error")
    numbers, count, summary, lowest, highest, avg, median = calculate(num_arr)

    
    print(f'numbers: {str(numbers)}')


    print('count = ' + str(count) + ' sum = ' + str(summary) + ' lower = ' + str(lowest) \
        + ' heighest = ' + str(highest) + ' mean = ' + str(avg))
    print(count, summary, lowest, highest, avg, median)