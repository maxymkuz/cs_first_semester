import calendar


def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    return s1.count(ch) + s2.count(ch)


def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("Кит кота по хвилях катав - кит кіт на киті.", "ки")
    'диво кит кота по хвилях катав - диво кит кіт на диво киті.'
    """
    sentence = sentence.lower()
    res_string = sentence.replace(flag, "диво " + flag)
    return res_string


def semester_calendar(output_type, year, first_month, last_month):
    """
    (str, int, int, int) -> str
    >>> semester_calendar("txt", 2016, 2, 3)
       February 2016
    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29
    <BLANKLINE>
         March 2016
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30 31
    <BLANKLINE>
	>>> semester_calendar("txt", 2020, 2, 3)
	   February 2020
	Mo Tu We Th Fr Sa Su
	                1  2
	 3  4  5  6  7  8  9
	10 11 12 13 14 15 16
	17 18 19 20 21 22 23
	24 25 26 27 28 29
	<BLANKLINE>
	     March 2020
	Mo Tu We Th Fr Sa Su
	                   1
	 2  3  4  5  6  7  8
	 9 10 11 12 13 14 15
	16 17 18 19 20 21 22
	23 24 25 26 27 28 29
	30 31
	<BLANKLINE>
    """
    res = ""
    if output_type == "txt":
        cal = calendar.TextCalendar(firstweekday=0)
        for i in range(first_month, last_month + 1):
            res += cal.formatmonth(year, i, 0, 0) + '\n'
            res = res[:-1]
        return print("  " + res[1:])
    elif output_type == "html":
        pass


# print(semester_calendar("txt", 2020, 2, 3))


if __name__ == "__main__":
    import doctest
    doctest.testmod()





	#cal = calendar.TextCalendar(firstweekday=0)
	# if output_type == "txt"
	# 	# res = ""
	# 	for i in range(first_month, last_month + 1):
	# 		res += cal.formatmonth(year, i, 0, 0)
	# 	return print(res)
	# elif output_type == "html":
	# 	pass