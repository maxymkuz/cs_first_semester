import sys


def return_digits(number):
    """ str -> str

    Preconditions: number.isdigit() == True
    Returns a string that represents the input string via visual art.

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

    try:
        digits = str(number)
        row = 0
        res = ""
        while row < 7:
            line = ""
            column = 0
            while column < len(digits):
                number = int(digits[column])
                digit = Digits[number]
                column += 1
                x = []
                temp = ''
                for i in range(len(digit[row])):
                    if digit[row][i] == "*":
                        x.append(i)
                for i in range(len(digit[row])):
                    if i in x:
                        line += str(number)
                    else:
                        line += " "
            if row != 6:
                res += line + "\n"
            else:
                res += line 
            row += 1
        return res
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)


if __name__ == "__main__":
    try:
        n = sys.argv[1]
        print(return_digits(n))
    except:
        pass
    # print(return_digits('123'))
    import doctest
    doctest.testmod()