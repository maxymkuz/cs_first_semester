def generate_number(number, digit, position):
    """
    (int,int,int) -> int
    :param number: (integer): number that will be changed
    :param digit: (integer): digit that will replace figure on position if it is bigger than it
    :param position: (integer): the position we will check 
    Precondition: 0 <= digit <= 9; position > 0
    Function returns the number, where figure on exact position is replaced by 'digit',
        if the figure on that position is lower than digit itself
    >>> generate_number(3746, 5, 0)
    3746
    >>> generate_number(3746, 5, 1)
    3756
    >>> generate_number(3746, 5, 2)
    3746
    >>> generate_number(3746, 5, 3)
    5746
    >>> generate_number(3746, 5, 4)
    53746
    >>> generate_number(3746, 5, 7)
    50003746
    """

    array = 0
    number_negative = True
    if number < 0:
        number_negative = False
        number = abs(number)
    
    x = number

    for i in range(position):
        x = x/(10)
        y = int(x)
        last_digit = round((x - y)*10)
        array += last_digit * (10 ** i)
        x = int(x)
    

    rest = int(x/(10))*(10**position)*10
    super_last_digit = int((x/10 - int(x/10))*10) 
    before_pos = int(x/(10))*10  

    if ((super_last_digit) < digit):
        super_last_digit = digit 

    x = before_pos*(10**position) + array + super_last_digit*(10**(position))

    return x if number_negative else -x




