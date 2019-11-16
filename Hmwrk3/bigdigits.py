import sys


def return_digits(number):
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
                    
                
            print(line)
            row += 1
    except IndexError:
        print("usage: bigdigits.py <number>")
    except ValueError as err:
        print(err, "in", digits)


return_digits(41072819)