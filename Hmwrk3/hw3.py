import doctest
import calculator
print(calculator.calculate([2, 4, 6, 7, 3]))

def is_power_of_two(val):
    """
    (int) -> bool

    Determine if a number is a power of two.

    >>> is_power_of_two([0])

    >>> is_power_of_two("0")

    >>> is_power_of_two(0)
    False
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(15)
    False
    >>> is_power_of_two(16)
    True
    """
    if not isinstance(val, int):
        return None
    for i in range(val):
        if 2 ** i == val:
            return True
    return False


def has_unique_chars(string):
    """
    (str) -> bool
     
    An algorithm to determine if a string has all unique characters.
     
    >>> has_unique_chars(None)
    False
    >>> has_unique_chars('')
    True
    >>> has_unique_chars('foo')
    False
    >>> has_unique_chars('bar')
    True
    """
    if not isinstance(string, str):
        return False
    for i in string:
        if string.count(i) > 1:
            return False
    return True


def compress(string):
    """
    (str) -> str

    Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

    >>> compress(None)

    >>> compress('')
    ''
    >>> compress('AABBCC')
    'AABBCC'
    >>> compress('AAABCCDDDDE')
    'A3BC2D4E'
    >>> compress('BAAACCDDDD')
    'BA3C2D4'
    >>> compress('AAABAACCDDDD')
    'A3BA2C2D4'
    """    
    temp = string
    if not isinstance(string, str):
        return None
    for i in range(len(string) + 1, 1, -1):
        for j in range(65, 123):
            to_replace = chr(j) * i        
            string = string.replace(to_replace, chr(j) + str(i))
    return temp if len(temp) == len(string) else string

import doctest
doctest.testmod()