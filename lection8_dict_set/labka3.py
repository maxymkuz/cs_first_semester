def dict_reader_tuple(file_dict):
    with open(file_dict, 'r', encoding='utf-8') as f:
        res = []
        for line in f:
            line = line.strip().split()
            tpl = (line[0], line[1], line[2:])
            res.append((line[0], line[1], line[2:]))
    return res


def dict_reader_dict(file_dict):
    dictionary = {}
    with open(file_dict, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip().split()
            print(line[0], line)
            dictionary
            # dictionary[line[0]] = set(dictionary[line[0]])
    print(dictionary)


dict_reader_dict('cmudict2.txt')


def dict_invert(dct):
    pass
