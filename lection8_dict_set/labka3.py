def dict_reader_tuple(file_dict):
    with open(file_dict, 'r', encoding='utf-8') as f:
        ans = [(line.strip().split()[0], line.strip().split()[1], line.strip().split()[2:]) for line in f]
    return ans


def dict_reader_dict(file_dict):
    dictionary = {}
    with open(file_dict, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split()
            if line[0] not in dictionary:
                x = set()
                x.add(tuple(line[2:]))
                dictionary[line[0]] = x
            else:
                temp = dictionary.get(line[0])
                temp.add(tuple(line[2:]))
    return dictionary


# print(dict_reader_dict('cmudict2.txt'))


def dict_invert(dct):
    """
    >>> dict_invert({'WATER':{('W','A','T','E','R')}})
    {1: {('WATER', ('W','A','T','E','R'))}}
    """
    if isinstance(dct, dict):
        