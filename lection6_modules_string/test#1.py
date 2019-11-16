import calendar

def semester_calendar(output_type, year, first_month, last_month):
    res = ""
    print(output_type)
    if output_type == "txt":
        cal = calendar.TextCalendar(firstweekday=0)
        for i in range(first_month, last_month + 1):
            res += cal.formatmonth(year, i, 0, 0)
        return res

    elif output_type == "html" :
        cal = calendar.HTMLCalendar(firstweekday=0)
        cal_format = cal.formatmonth(year ,first_month)
        return cal_format


print(semester_calendar("html", 2016, 2, 3))


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
