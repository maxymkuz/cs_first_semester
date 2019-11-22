def dict_reader_tuple(file_dict):
    with open(file_dict, 'r', encoding='utf-8') as f:
        return [(line.strip().split()[0], int(line.strip().split()[1]), line.strip().split()[2:]) for line in f]


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
def list_to_dict(lst):
    dct = {i[0]: set() for i in lst}
    for i in lst:
        dct[i[0]].add((tuple(i[2])))
    return dct


def dict_invert(dct):
    """
    Return a dictionary, not depending whether the list or 
    dictionary was an argument

    >>> dict_invert({'WATER':{('W', 'A', 'T', 'E', 'R')}})
    {1: {('WATER', ('W', 'A', 'T', 'E', 'R'))}}
    >>> dict_invert([("NACHOS", 1, ["N", "AA1", "CH", "OW0", "Z"])])
    {1: {('NACHOS', ('N', 'AA1', 'CH', 'OW0', 'Z'))}}
    >>> dict_invert({'NACHOS':{("N", "AA1", "CH", "OW0", "Z")}})
    {1: {('NACHOS', ('N', 'AA1', 'CH', 'OW0', 'Z'))}}
    """
    if isinstance(dct, list):
        dct = list_to_dict(dct)
    res = {}
    for key in dct:
        n = len(dct[key])
        for i in range(n):
            if n not in res:
                res[n] = set()
            res[n].add((key, tuple(dct[key])[i]))

    res_sorted = {key: res[key] for key in sorted(res.keys())}
    return res_sorted


# print(dict_invert(dict_reader_tuple('cmudict2.txt')) == 
# dict_invert(dict_reader_dict('cmudict2.txt')))
