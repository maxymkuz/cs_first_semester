def weekday_name(number):
    """
    int -> str
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    """
    arr_of_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    return arr_of_days[number]


	
def weekday(date):
    """
    str -> int
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError 
    with corresponding message
                                                
    >>> weekday("12.08.2015")
    2
                                      
    """
    splitted = date.split(".")
    
    day = int(splitted[0])
    month = int(splitted[1])
    year = int(splitted[2])
    if month >= 3:
        ans = (day + ((13 * (month + 1)) // 5) + year % 100 +
                ((year % 100) // 4) +
                ((year // 100) // 4) -
                2 * (year // 100) - 2)
    else:
        year -= 1
        ans = (day + ((13 * (month + 13)) // 5) + year % 100 +
                ((year % 100) // 4) +
                ((year // 100) // 4) -
                2 * (year // 100) - 2)

    return ans % 7


def count_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        num_of_days = 31
    if month in [4, 6, 9, 11]:
        num_of_days = 30
    elif month == 2:
        if year % 4 == 0:
            num_of_days = 29 if year % 100 != 0 or year % 400 == 0 else 28
    return num_of_days

def calendar(month, year):
    """
    (int, int) -> str
    Return a string representing a calendar for given month and year
    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in weekday 
           works correctly only for Gregorian calendar, so year must 
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message
    
    >>> print(calendar(8 , 2015))
    The calendar is:
    mon    3  10 17 24 31
    tue    4  11 18 25
    wed    5  12 19 26
    thu    6  13 20 27
    fri    7  14 21 28
    sat 1  8  15 22 29
    sun 2  9  16 23 30
    """
    array = [[], [], [], [], [], [], []]
    res = 'The calendar is:\n'

    num_of_days = count_days(month)


    for j in range(1, num_of_days + 1):  # numbers are sorted depending on which day of the week it is
        number = weekday(str(j) + "." + str(month) + "."+ str(year))
        array[number].append(j)  #appending this num to his place in array

    #cheching which day of week is the first day of the month
    first_day = weekday("01." + str(month) + "."+ str(year)) 
    print(array)


    for i in range(7):
        name_of_the_day = weekday_name(i) + ' '  # mon/tue/wed/...

        if i < first_day:
            name_of_the_day += '   '  # if there has to be nothing in the first week
        for date in range(len(array[i])):
            if array[i][date] < 10:  # if we have to add additional space
                name_of_the_day += str(array[i][date]) + '  '  # adding day and two spaces 
            else:
                name_of_the_day += str(array[i][date]) + ' '  # adding day and only one space      
        res += name_of_the_day.rstrip() + '\n' #adding one more line to the answer
    res = res.rstrip() #deleting unnesessary spaces
    return res



def reversed_calendar(month, year):
    """
    (int, int) -> str
    Return a string representing a calendar for given month and year
    month : an integer in range[1 , 12]
    year : an integer (strictly speaking the algorithm in weekday 
           works correctly only for Gregorian calendar, so year must 
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message
    >>> print(reversed_calendar(4, 2016))
        The calendar is:
    mon tue wed thu fri sat sun
                      1   2   3
     4   5   6   7   8   9  10
    11  12  13  14  15  16  17
    18  19  20  21  22  23  24
    25  26  27  28  29  30
    >>> print(reversed_calendar(6, 2019))
         The calendar is:
    mon tue wed thu fri sat sun
                          1   2
     3   4   5   6   7   8   9
    10  11  12  13  14  15  16
    17  18  19  20  21  22  23
    24  25  26  27  28  29  30
    """
    array_of_dates =  [[], [], [], [], [], [], []]
    res = 'The calendar is:\n'
    num_of_days = count_days(month)

    for j in range(1, num_of_days + 1):  # numbers are sorted depending on which day of the week it is
        number = weekday(str(j) + "." + str(month) + "."+ str(year))
        array_of_dates[number].append(j)  #appending this num to his place in array
    

    #cheching which day of week is the first day of the month
    first_day = weekday("01." + str(month) + "."+ str(year)) 
    was_start = False
    temporary_str = '     The calendar is:\nmon tue wed thu fri sat sun \n'
    number = 0
    x = 0
    while True:
        for i in range(7):
            if number == num_of_days:
                break
            if x < first_day :
                temporary_str += "    "
                x += 1
            else: 
                number += 1
                if number < 10:
                    temporary_str += "  " + str(number) + " " 
                else:
                    temporary_str += " " + str(number) + " "
        if number == num_of_days:
                break
        temporary_str += "\n"
    return temporary_str





# if __name__ == '__main__':
#     try:
#         print("Type month")
#         month = input()
#         month = int(month)
#         print("Type year")
#         year = input()
#         year = int(year)
#         print("\n\nThe calendar is: ")
#         print (calendar(month, year)) 
#     except ValueError as err:
#         print(err)
