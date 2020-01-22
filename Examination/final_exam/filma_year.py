def read_file(path):
    """
    (str) -> (list)
    Return a ilst of lines from file
    """

    # , encoding="utf-8"
    lines = []
    with open(path, "r", encoding="utf-8", errors="ignore") as file:
        i = 0

        for line in file:
            if i < 15:
                i += 1
                continue
            i += 1
            # line = list(filter(lambda x: len(x) > 0, line.strip().split("\t")))
            line = line.strip().split("\t")
            lines.append(line)
    return lines


def country_dict(lines_list, year):
    dct = {}
    for film in lines_list:
        
        # print(film)
        start = False
        year = ""
        for i in film:
            if i == '(':
                start = True
            elif i == ')':
                start = False
            elif start:
                print("here:")
                year += i
        print(year)
        x = film[0].split('"')
        name = ""
        name = x[0]
        country = film[-1]

        try:
            # print(film[1])
            year_1 = int(film[1][1:5])
        except:
            continue
        print(name, country, year)


country_dict(read_file("countries.list"), 2002)
# def films_year():
#     pass