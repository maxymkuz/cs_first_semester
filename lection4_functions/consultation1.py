def three_digit(number):
    """
    int -> bool
    Returns true if all digins are divisions of this num
    """

    number = abs(number)

    if not isinstance(number, int):
        return False

    if number % 1000 != number:
        return False

    digits = []
    while number > 0 :
        number, rev = divmod(number, 10)
        if rev not in digits:
            digits.append(rev)
    if len(digits) != 3:
        return False
    count = 0 
    for item in digits:
        count += number % item
    return False if count != 0 else True


print(three_digit(122))
