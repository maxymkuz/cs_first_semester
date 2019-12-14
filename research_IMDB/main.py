import time


time0 = time.time()


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


def make_dict_from_ratings():
    """
    None -> dict
    Returns a dictionary with info from ratings.list
    """
    counter, suma = 0, 0
    line_number = 0
    dic = {}
    last_title = ""

    for line in open("ratings.list", "r", encoding="ISO-8859-1"):

        # checking is we are in right line
        if 664580 < line_number or line_number < 297:
            line_number += 1
            continue
        line_number += 1

        line = line.strip().split()

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

        title = concatenate_list(title_year[:-1])
        try:
            year = int(title_year[-1][1:5])
        except ValueError:
            continue

        # All the TV series will be counted overall, not by episodes
        if last_title == title:
            continue
        last_title = title

        dic[title] = [num_of_votes, rating, year]
    return dic


# print(dicrionary["Rick and Morty"])


###############################################################################


def add_genres(dictionary_without):
    """
    dict -> dict
    Receives a dict from previous function and then
    adds unique genres to only films with genres
    """
    dictionary = {}
    previous_title = ""
    genres = set()
    conter = 0
    line_number = 1
    for line in open("genres.list", 'r', encoding="ISO-8859-1"):
        # checking is we are in right line
        if line_number < 381:
            line_number += 1
            continue
        line_number += 1

        line = line.strip().split("\t")
        while "" in line:
            line.remove("")
        tit = line[0].split()
        title = ""
        lst_trial = []

        for i in range(len(tit)):
            if tit[i][0] == "(":
                break
            lst_trial.append(tit[i])
        title = concatenate_list(lst_trial)
        genre = line[-1]

        # checking if there are multiple genres of exact thing
        if previous_title == title:
            genres.add(genre)
        else:
            to_append = tuple(genres)
            if previous_title in dictionary_without:
                dictionary_without[previous_title].append(to_append)
                dictionary[previous_title] = dictionary_without[previous_title]

            genres.clear()
            genres.add(genre)
        previous_title = title
    return dictionary


###############################################################################


def create_dict_file(dicrionary):
    """
    This func is used for simplicity and speed
    """
    f = open("stuff/dictionary.txt", "w+", encoding="ISO-8859-1")
    for key in dictionary:
        string = key + "\t" + str(dicrionary[key][0]) + " " +\
        str(dicrionary[key][1]) + " " + str(dictionary[key][2])

        string += " " + concatenate_list(list(dicrionary[key][3])) + "\n"
        f.write(string)
    f.close()


def get_dict_from_file():
    dictionary = {}
    for line in open("stuff/dictionary.txt", 'r', encoding="ISO-8859-1"):
        line = line.strip().split("\t")
        line1 = line[1].split()
        title = line[0]
        dictionary[title] = line1
        # rest = line
        # print(line)
    return dictionary


###############################################################################


def get_avg_year_num_of_votes(dct, year):
    """
    int -> int
    """
    counter, suma = 0, 0
    for key in dct:
        if str(year) in dct[key]:
            counter += 1
            suma += int(dct[key][0])
    return suma/counter


def get_stats_across_years(dct):
    avg_number_dict = {}
    for year in range(1970, 2016):
        avg_number_dict[year] = get_avg_year_num_of_votes(dct, year)
    return avg_number_dict


def get_genre_year_votes(dct, genre, year):
    """
    dict, int, genre -> dict
    Analyses given ganre in given year and makes calculations
    """
    counter = 0
    num_of_votes = 0
    for key in dct:
        if genre in dct[key] and str(year) in dct[key]:
            counter += 1
            num_of_votes += float(dct[key][0])
    # print(genre, year, num_of_votes/counter)
    return num_of_votes  # /counter


def get_average_num_of_votes(vote_dict):
    counter, suma = 0, 0
    for key in vote_dict:
        counter += 1
        suma += vote_dict[key]
    return suma/counter


if __name__ == "__main__":
    genres_list = ["Adventure", "Sci-Fi", "Fantasy", "Thriller", "Action",
                   "Crime", "Mystery", "Comedy", "Documentary", "Adult", 
                   "Romance", "Animation", "Family", "Horror",
                   "Biography", "History", "Sport", "Musical",
                   "War", "Western", "Music"]
    small_genres_list = ["Documentary", "Animation", "Comedy"]

    result = {}

    # dictionary_without = make_dict_from_ratings()
    # dictionary = add_genres(dictionary_without)
    # create_dict_file(dictionary)

    dictionary = get_dict_from_file()
    avg_number_dict = get_stats_across_years(dictionary)
    print(avg_number_dict)

    for genre in small_genres_list:
        result[genre] = {}
        for year in range(1970, 2016):
            result[genre][year] = get_genre_year_votes(dictionary, genre, year)
        avg_in_genre = get_average_num_of_votes(result[genre])
        print(avg_in_genre, genre)

    # for key in result["Comedy"]:
    #     print(key, result["Comedy"][key]/avg_number_dict[key])

    # x = final(dictionary, 1970)
    # print(x)
    print(result["Documentary"])
    print(avg_number_dict)
