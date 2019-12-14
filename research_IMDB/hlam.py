def concatenate_list(lst):
    """
    lst -> str
    Reseives list of strings and returns a concatenated string
    """
    result = ''
    for element in lst:
        result += element + " "
    result = result.strip()

    # removing double quotation marks form beginning and end

    try:
        if result[0] == '"':
            result = result[1:]
        if result[-1] == '"':
            result = result[:-1]
    except IndexError:
        pass

    return result


###############################################################################


def date_name():
    string = ""
    for line in open("./IMDB/movies.list", "r"):
        res = line.strip().split()
        prev_str = string
        string = ""
        flag = False
        for word in res:
            for symbol in word:
                if symbol == '"' and not flag:
                    flag = True
                    string = ""
                elif symbol == '"':
                    flag = False
                    break
                elif flag:
                    string += symbol
        if prev_str != string:
            print(res[-1] + " " + string)


# date_name()


def get_actors():
    res = []
    for line in open("actors.list", "r"):
        line = line.strip()
        if(len(line) < 1):
            user = []
        else:
            print(line[0])


###############################################################################


def get_avg_year_rating(year):
    """
    int -> int
    """
    counter, suma = 0, 0
    line_number = 0
    for line in open("ratings_small.list", "r"):
        if 664580 < line_number or line_number < 297:
            line_number += 1
            continue
        line_number += 1

        line = line.strip().split(" ")
        while "" in line:
            line.remove("")

        len_of_title = 0
        for i in range(3, len(line)):
            if line[i][0] == "{":
                break
            else:
                len_of_title += 1

        if line[-1] == "(V)" or line[-1] == "(TV)" or line[-1] == "(VG)":
            len_of_title -= 1

        num_of_votes = int(line[1])
        rating = float(line[2])

        title_year = line[3: 3+len_of_title]

        title = concatenate_list(title_year[0:-1])
        try:
            current_year = int(title_year[-1][1:5])
        except ValueError:
            continue
        if current_year == year:
            counter += 1
            suma += rating
    print(year, suma/counter)


###############################################################################


def get_avg_year_num_of_votes(year):
    """
    int -> int
    """
    counter, suma = 0, 0
    line_number = 0
    for line in open("ratings.list", "r"):
        if 664580 < line_number or line_number < 297:
            line_number += 1
            continue
        line_number += 1

        line = line.strip().split(" ")
        while "" in line:
            line.remove("")

        len_of_title = 0
        for i in range(3, len(line)):
            if line[i][0] == "{":
                break
            else:
                len_of_title += 1

        if line[-1] == "(V)" or line[-1] == "(TV)" or line[-1] == "(VG)":
            len_of_title -= 1

        num_of_votes = int(line[1])
        rating = float(line[2])

        title_year = line[3: 3+len_of_title]

        title = concatenate_list(title_year[0:-1])
        try:
            current_year = int(title_year[-1][1:5])
        except ValueError:
            continue
        if current_year == year:
            counter += 1
            suma += num_of_votes
    print(year, suma/counter)


def get_stats_across_years():
    for year in range(1948, 2016):
        # get_avg_year_rating(year)
        get_avg_year_num_of_votes(year)


def final(dct, year):
    """
    dict, int -> dict
    Analyses every ganre and makes calculations
    """
    genres_dict = {}
    genres_list = ["Comedy", "Documentary", "Adult", "Action",
                   "Thriller", "Romance", "Animation", "Family", "Horror",
                   "Music", "Crime", "Adventure", "Sci-Fi", "Fantasy",
                   "Mystery", "Biography", "History", "Sport", "Musical",
                   "War", "Western"]

    for i in genres_list:
        genres_dict[i] = [1, 0, 0]

    for key in dct:
        for genre in genres_list:
            if genre in dct[key] and str(year) in dct[key]:
                genres_dict[genre][0] += 1
                genres_dict[genre][1] += float(dct[key][2])
            genres_dict[genre][2] = genres_dict[genre][1]/genres_dict[genre][0]
    return genres_dict
