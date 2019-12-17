import time
import matplotlib.pyplot as plt
import numpy as np

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


def get_average(d):
    suma = 0
    for key in d:
        suma += d[key]
    return round(suma/len(d), 4)


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

    for line in open("ratings_genres/ratings.list", "r", encoding="ISO-8859-1"):

        # checking is we are in the right line
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

        # if line ends with bad symbols, don't count them
        if line[-1] == "(V)" or line[-1] == "(TV)" or line[-1] == "(VG)":
            len_of_title -= 1

        num_of_votes = int(line[1])
        rating = float(line[2])
        title_year = line[3: 3+len_of_title]
        title = concatenate_list(title_year[:-1])

        # check if the year is a 4-digit integer
        try:
            year = int(title_year[-1][1:5])
        except ValueError:
            continue

        # All the TV series will be counted overall, not by episodes
        if last_title == title:
            continue
        last_title = title

        # forming a resulting dictionary with key--list
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
    line_number = 1

    for line in open("ratings_genres/genres.list", 'r', encoding="ISO-8859-1"):

        # checking if we are in right line(if there's useful data in that line)
        if line_number < 381:
            line_number += 1
            continue
        line_number += 1

        line = line.strip().split("\t")

        # removing all the blank elems in list
        while "" in line:
            line.remove("")

        # Getting a title of a movie:
        tit = line[0].split()
        title = ""
        lst_trial = []

        for i in range(len(tit)):

            # if elem starts with "(", then it's year elem
            if tit[i][0] == "(":
                break
            lst_trial.append(tit[i])

        title = concatenate_list(lst_trial)
        genre = line[-1]

        # checking if there are multiple genres of one movie/series
        if previous_title == title:
            genres.add(genre)
        else:
            to_append = tuple(genres)
            if previous_title in dictionary_without:
                dictionary_without[previous_title].append(to_append)
                dictionary[previous_title] = dictionary_without[previous_title]
            genres.clear()
            genres.add(genre)

        # to prevent counting tv-series multiple times
        previous_title = title

    return dictionary


###############################################################################


def create_dict_file(dicrionary):
    """
    dict -> None
    This func is used for simplicity and speed (used it while I've developed
    a program in order not to wait for long every time)
    """
    f = open("dictionary.txt", "w+", encoding="ISO-8859-1")

    for key in dictionary:
        string = key + "\t" + str(dicrionary[key][0]) + " " +\
                 str(dicrionary[key][1]) + " " + str(dictionary[key][2])
        string += " " + concatenate_list(list(dicrionary[key][3])) + "\n"
        f.write(string)

    f.close()


def get_dict_from_file():
    """
    None -> dict
    This func is used for simplicity and speed (used it while I've developed
    a program in order not to wait for long every time, I've maid a file with
    results of first and second function)

    The problem is, it won't return integers and that's why
    currently it is useless
    """
    dictionary = {}

    for line in open("dictionary.txt", 'r', encoding="ISO-8859-1"):
        line = line.strip().split("\t")
        line1 = line[1].split()
        title = line[0]
        dictionary[title] = line1

    return dictionary


###############################################################################


def get_year_sum_of_votes(dct, year):
    """
    dict, int -> int
    Returns a number, which is the sum of all votes of all genres
    in given year
    """
    suma = 0

    for key in dct:
        if year in dct[key]:
            suma += int(dct[key][0])

    return suma


def get_stats_across_years(dct):
    """
    dict -> dict
    Uses previous function to return a dictionary with average number
    of votes from all genres
    """
    avg_number_dict = {}

    for year in range(1950, 2016):
        avg_number_dict[year] = get_year_sum_of_votes(dct, year)

    return avg_number_dict


###############################################################################


def get_genre_year_votes(dct, genre, year):
    """
    dict, int, genre -> dict
    Analyses given genre in given year and  returns sum of
    number of all votes
    """
    num_of_votes = 0

    for key in dct:
        if genre in dct[key][-1] and year in dct[key]:
            num_of_votes += float(dct[key][0])

    return num_of_votes


###############################################################################


def make_visualization_dict(result):
    """
    dict -> dict
    Returns a dict with all the information needed for matprolib
    from and adjusted for visualization
    """
    final_dict = {}

    for genre in result:
        final_dict[genre] = [[], [], [], 0]

        for year in result[genre]:
            final_dict[genre][0].append(year)
            final_dict[genre][1].append(result[genre][year])
        final_dict[genre][2] = [get_average(result[genre])]*len(result[genre])
        final_dict[genre][3] = sum(final_dict[genre][2])/(2015-1950)

    return final_dict


def visualize(result, x):
    """
    dict, string -> None
    This function is used to visualise all the data:
    1) Graphs with 8 major genres and their popularity across years
    2) A chart, which represents the percentage of films
    with different genres in the history
    """
    final_dict = make_visualization_dict(result)

    # Adjusting the size of the window

    # First 8 are figures with single genre:
    if x == "0":

        fig = plt.figure(figsize=(20, 8))

        ax = fig.add_subplot(331)

        ax.plot(final_dict["Action"][0], final_dict["Action"][2],
                color='red',
                label='average')
        ax.plot(final_dict["Action"][0], final_dict["Action"][1],
                color='green', label='Action')

        ax.legend()

        # Thriller:
        ax2 = fig.add_subplot(332)

        ax2.plot(final_dict["Thriller"][0], final_dict["Thriller"][1],
                 color='blue', label='Thriller')
        ax2.plot(final_dict["Thriller"][0], final_dict["Thriller"][2],
                 color='red',
                 label='average')

        ax2.legend()

        # Adventure:
        ax3 = fig.add_subplot(333)

        ax3.plot(final_dict["Adventure"][0], final_dict["Adventure"][2],
                 color='red', label='average')
        ax3.plot(final_dict["Adventure"][0], final_dict["Adventure"][1],
                 color='green', label='Adventure')

        ax3.legend()

        # Crime:
        ax4 = fig.add_subplot(334)

        ax4.plot(final_dict["Crime"][0], final_dict["Crime"][2],
                 color='red', label='average')
        ax4.plot(final_dict["Crime"][0], final_dict["Crime"][1],
                 color='blue', label='Crime')

        ax4.legend()

        # Sci-fi:
        ax5 = fig.add_subplot(335)

        ax5.plot(final_dict["Sci-Fi"][0], final_dict["Sci-Fi"][1],
                 color='green', label='Sci-Fi')
        ax5.plot(final_dict["Sci-Fi"][0], final_dict["Sci-Fi"][2],
                 color='red', label='average')

        ax5.legend()

        # Fantasy:
        ax6 = fig.add_subplot(336)

        ax6.plot(final_dict["Fantasy"][0], final_dict["Fantasy"][2],
                 color='red', label='average')
        ax6.plot(final_dict["Fantasy"][0], final_dict["Fantasy"][1],
                 color='blue', label='Fantasy')

        ax6.legend()

        # Mystery
        ax7 = fig.add_subplot(337)

        ax7.plot(final_dict["Mystery"][0], final_dict["Mystery"][2],
                 color='red', label='average')
        ax7.plot(final_dict["Mystery"][0], final_dict["Mystery"][1],
                 color='green', label='Mystery')

        ax7.legend()

        # Western -- it's not that popular, just interesting
        ax8 = fig.add_subplot(338)

        ax8.plot(final_dict["Western"][0], final_dict["Western"][2],
                 color='red', label='average')
        ax8.plot(final_dict["Western"][0], final_dict["Western"][1],
                 color='blue', label='Western')

        ax8.legend()

        plt.show()

        # Now it's a chart with info about all the most popular films:
        ax10 = fig.add_subplot(339)
        # Placeholders:
        people = ('Action', 'Thriller', 'Adventure', 'Crime', 'Sci-Fi',
                  'Fantasy', 'Mystery')
        y_pos = np.arange(len(people))
        # Array with percentage of films of this genre
        # I made a function, where I've received this, and in order to
        # make computing faster, just copypasted it
        performance = [29.9980, 27.9372, 23.8616, 19.2558, 18.7932,
                       15.2791, 10.0164]
        error = np.random.rand(len(people))

        # Just configurations
        ax10.barh(y_pos, performance, xerr=error, align='center')
        ax10.set_yticks(y_pos)
        ax10.set_yticklabels(people)
        # labels read top-t|o-bottom
        ax10.invert_yaxis()
        # Placeholders
        ax10.set_xlabel('Percentage, in %')
        ax10.set_title('Percentage of films with this genre')

    elif x == "1":

        fig = plt.figure(figsize=(10, 8))

        # Now it's a chart with info about all the most popular films:
        ax = fig.add_subplot(111)

        # Placeholders:
        people = ('Action', 'Thriller', 'Adventure', 'Crime', 'Sci-Fi',
                  'Fantasy', 'Mystery')

        y_pos = np.arange(len(people))

        # Array with percentage of films of this genre
        # I made a function, where I've received this, and in order to
        # make computing faster, just copypasted it
        performance = [29.9980, 27.9372, 23.8616, 19.2558, 18.7932,
                       15.2791, 10.0164]

        error = np.random.rand(len(people))

        # Just configurations
        ax.barh(y_pos, performance, xerr=error, align='center')

        ax.set_yticks(y_pos)
        ax.set_yticklabels(people)

        # labels read top-t|o-bottom
        ax.invert_yaxis()

        # Placeholders
        ax.set_xlabel('Percentage, in %')
        ax.set_title('Percentage of films with this genre')

        plt.show()


def main():
    """
    Main func that is used to call all other funcs and
    finally, visualize the data
    """

    print("Welcome!")
    print("   0 - If You want to see charts of popularity of 8 genres across\
 years, type 0")
    print("   1 - If You want to see figure of most popular genres ever\
 , type 1")
    while True:
        x = input()
        if x == "1" or x == "0":
            break
        print("You have to type either 1 or 0")

    print("This python script analyses data from IMDB databases from\
1950 till 2015 years\n and returns 9 charts with popularity of some\
of the most popular genres\n")

    print("In order to receive the result, you have to wait for some time")
    print("It takes appriximately 2 min to get in done on my linux machine\n")
    genres_list = ["Adventure", "Sci-Fi", "Fantasy", "Thriller", "Action",
                   "Crime", "Mystery", "Comedy", "Documentary", "Adult",
                   "Romance", "Animation", "Family", "Horror",
                   "Biography", "History", "Sport", "Musical",
                   "War", "Western", "Music"]
    small_genres_list = ["Adventure", "Sci-Fi", "Fantasy", "Thriller",
                         "Action", "Crime", "Mystery", "Western"]

    result = {}

    print("Searching for ratings for each movie/TV-series...")

    dictionary_without = make_dict_from_ratings()  # 3.9614

    print("Adding genres...")

    dictionary = add_genres(dictionary_without)  # 10.6271

    # Average votes across years:
    print("Finding average number of votes per year..")

    avg_number_dict = get_stats_across_years(dictionary)  # 10.6446

    # Forming a result with all info, ready for visualization
    print("Getting year/genre data ready. Please wait till the end,\
 it'll be worth it!")

    for genre in small_genres_list:
        print(f"Analyzing genre: {genre}. Wait for a few more seconds")
        result[genre] = {}

        for year in range(1950, 2016):
            votes_percent = get_genre_year_votes(dictionary, genre, year)*100
            # dividing on average num of votes in that year:
            result[genre][year] = round(votes_percent/avg_number_dict[year], 4)

    print("Visualizing...")
    # print(result)
    visualize(result, x)


###############################################################################


if __name__ == "__main__":

    main()
