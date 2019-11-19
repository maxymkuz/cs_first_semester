file = open("dob.txt", "r", encoding="utf-8")
lines = file.readlines()
# print(lines)
# for line in file:
#     print(line + '\n')
# print(f + '\n')

a = 2
b = a
a = 12
# print(id(a))
# print(id(b))


import sys
def return_digits(number):
    """
    >>> return_digits(123)
    ' 1  222  333 \\n11 2   23   3\\n 1 2  2     3\\n 1   2    33 \\n 1  2       3\\n 1 2    3   3\\n11122222 333 '
    >>> return_digits(6)
    ' 666 \\n6    \\n6    \\n6666 \\n6   6\\n6   6\\n 666 '
    >>> return_digits('')
    '\\n\\n\\n\\n\\n\\n'
    """
    Zero = ["  ***  ",
            " *   * ",
            "*     *",
            "*     *",
            "*     *",
            " *   * ",
            "  ***  "]
    One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
    Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
    Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
    Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
    Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
    Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
    Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
    Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
    Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
    Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]




    for i in range(7):
        for j in range(len(Digits)):
            Digits[j][i] = Digits[j][i].replace("*", str(j))
    try:
        digits = str(number)
        row = 0
        res=""
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                line += digit[row]
                column += 1
            
            if row == 6:
                res += line
            else:
                res += line + "\n"
            row += 1

        return res
        pass       
    except ValueError as err:
        print(err, "in", digits)
    

if __name__ == "__main__":
    try:
        digits = sys.argv[1]
        print(return_digits(digits))
    except IndexError:
        print("usage: bigdigits.py <number>")
    print(return_digits('123'))
    import doctest
    doctest.testmod()