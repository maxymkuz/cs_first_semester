def common_names(female_names, male_names):
    """
    (list, list) -> list

    returns a list of names that are in both lists

    >>> common_names([1, 2], [3, 5])
    set()
    >>> common_names(['al', 'aball', 'alll'], ['al', 'ball'])
    {'al'}
    """
    return set(female_names) & set(male_names)


def names_read(file_name):
    """
    str -> list

    returns a list of all names in file 'file_name'
    """
    res = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            res.append(line)
    return res


male_names = names_read('male.txt')
female_names = names_read('female.txt')
# print(common_names(['al', 'all', 'alll'], ['al', 'all']))
import doctest
doctest.testmod()