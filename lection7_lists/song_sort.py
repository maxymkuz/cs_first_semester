def song_length(x):
    """
    tuple -> float
    returns the second element of the tuple
    """
    return x[1]


def title_length(x):
    """
    tuple -> string
    returns the first element of the tuple
    """
    return len(x[0])


def last_word(x):
    """
    tuple -> string
    returns the last word of the first element of the tuple
    """
    return x[0].split()[-1]


def sort_songs(song_titles, length_songs, key):
    """
    (list, list, function) -> list
    returs a sorted list of elements by the third argument
    >>> sort_songs(["a b", "c", "d e", "f"], ['3', '5', '8', '7'],\
     title_length)
    [('c', '5'), ('f', '7'), ('a b', '3'), ('d e', '8')]
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені'],\
    ['3.19', '3.58', '5.06'], song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58'), ('Мало мені', '5.06')]
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені'],\
    ['3.19', '3.58', '5.06'], song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58'), ('Мало мені', '5.06')]
    """
    zipped = zip(song_titles, length_songs)
    x = sorted(zipped, key=key) 
    return x
