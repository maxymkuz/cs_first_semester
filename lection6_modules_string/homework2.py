#Problem 1
def get_position(ch):
    """
    str -> int
    Return a positon of letter in alphabet. If argument is not a letter function
    should return None.
    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')
    
    """
    if not isinstance(ch, str): return None 
    if len(ch) == 1:
        letter_order = ord(ch.upper()) - 64
        if  1 <= letter_order <= 26:
            return letter_order
    return None
# print(get_position(1258))

# ****************************************
# Problem 3
def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is larger
    than string s2 and False otherwise. If arguments aren't string or function
    have different length function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    try:
        for i in range(max(len(s1), len(s2))):
            if s1[i].upper() == s2[i].upper():
                continue
            if s1[i].upper() > s2[i].upper():
                return True
        return False     
    except:
        return None


# ****************************************
# Problem 4
def type_by_angles(a, b, c):
    """
    (float, float, float) -> str
    Detect the type of triangle by it's angles in degrees and return type as string
    ("right angled triangle", "obtuse triangle", "acute triangle"). If there is no
    triangle with such angles, then function should return None.

    >>> type_by_angles(60, 60, 60)
    'acute triangle'
    >>> type_by_angles(90, 30, 60)
    'right angled triangle'
    >>> type_by_angles(2015, 2015, 2015)

    """
    if a + b + c != 180:
        return None
    max_angle = max(a, b, c)
    if max_angle == 90:
        return "right angled triangle"
    return "obtuse triangle" if max_angle > 90 else "acute triangle"


# ****************************************
# Problem 6
def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    "I'll make him an offer he can't refuse."
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    'Great men are not born great, they grow great...'
    >>> remove_spaces(2015)

    """
    try:
        while True:
            if s.find("  ") == -1:
                break
            s = s.replace("  ", " ")
        return s
    except :
        return None



# ****************************************
# Problem 8
def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    if isinstance(s, str):
        return s.count(".")
    else: 
        return None


# ****************************************
# Problem 11
def decrypt_message(s):
    """
    str -> str
    Replace all letters in string with previous letters in aplhabet. If argument isn't a string
    function should return None.

    >>> decrypt_message("Sfwfohf jt b ejti uibu ubtuft cftu xifo tfswfe dpme.")
    'Revenge is a dish that tastes best when served cold.'
    >>> decrypt_message("Ofwfs ibuf zpvs fofnjft. Ju bggfdut zpvs kvehnfou.")
    'Never hate your enemies. It affects your judgment.'
    >>> decrypt_message(2015)

    """
    if isinstance(s, str):
        for i in range(64, 123, 1):
            s = s.replace(chr(i), chr(i - 1))
        return s
    return None



# ****************************************
# Problem 16
def find_union(s1, s2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    if isinstance(s1, str) and isinstance(s2, str):
        res = ""
        for i in range(65, 123):
            if chr(i) in s1 + s2:
                res += chr(i)
        return res
    return None


# ****************************************
# Problem 17
def number_of_occurence(lst, s):
    """
    (list, str) -> int
    Find and return number of occurence of string s in all elements of the
    list lst. If lst isn't list of strings or s isn't string function should
    return None.

    >>> number_of_occurence(["man", "girl", "women", "boy"], "m")
    2
    >>> number_of_occurence(["ab", "aba", "a", "b", "ba"], "ba")
    2
    >>> number_of_occurence([1, 2, 2015, 1, 3], "1")

    """
    counter = 0 
    for i in lst:
        if isinstance(i, str) and isinstance(s, str):
            counter += i.count(s)
        else:
            return None
    return counter


# ****************************************
# Problem 22
def pattern_number(sequence):
    """
    list -> list
    >>> pattern_number([])
    
    >>> pattern_number([42])
    
    >>> pattern_number([1,2])
    
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    
    >>> pattern_number([1,2,3,1,2,3])
    ([1, 2, 3], 2)
    >>> pattern_number([1,2,3,1,2])
    
    >>> pattern_number([1,2,3,1,2,3,1])
    
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')

    """
    number_of_ok = 1
    ok_value = 0
    length = len(sequence)

    for i in range(1, length):# i - number of items in sequence
        this_length_is_ok = True

        for sequence_elem in range(0, i):
            for check in range(0 + sequence_elem, length, i): # j - elems of sequence
                if sequence[check] != sequence[sequence_elem]:
                    this_length_is_ok = False

        if this_length_is_ok:
            number_of_ok += 1
            if ok_value == 0:
                ok_value = i

    res = sequence[0:ok_value]

    if number_of_ok == 1 or len(res) * number_of_ok != len(sequence):
        return None
    return res, number_of_ok
    

# ****************************************
# Problem 24
def numbers_Ulam(n):
    """
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    res = [1, 2]
    if not isinstance(n, int) or n ==0: return None
    number_to_check = 3 

    while len(res) < n:
        temporary_possible = []
        for value1 in res:
            for value2 in res:
                possible_number = value1 + value2
                if value1 >= value2 or possible_number in res: continue
                temporary_possible.append(possible_number)
        while True:
            if temporary_possible.count(number_to_check) == 1:
                res.append(number_to_check)
                break
            number_to_check += 1
    return [1] if n== 1 else res


# ****************************************
# Problem 25
def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    x = n 
    y = n
    next_number = 0
    tries = 0
    while next_number != 1:
        length = 0
        while x > 0:
            x = x // 10
            length += 1
        next_number = 0
        for i in range(length):
            next_number += ((y // 10**i)% 10)**2
        x ,y = next_number, next_number
        tries += 1
        if tries > 100000: return False
    return True


# ****************************************
# Problem 26
# ****************************************
def sum_of_divisors(n, lst):
    """
    (int, list) -> int
    Find and return sum of all odd numbers in the list, that are divisible by n.

    >>> sum_of_divisors(3, [2, 0, 1, 5])
    0
    >>> sum_of_divisors(5, [2, 0, 1, 5])
    5
    >>> sum_of_divisors(7, [])
    0

    """
    if not isinstance(n, int) and not isinstance(lst, list): return None
    res = 0
    for i in lst:
        if i%n == 0 and i%2 == 1:
            res += i
    return res




if __name__ == "__main__":
    import doctest
    doctest.testmod()


# for i, j in enumerate(lst):
#     print(i, j)