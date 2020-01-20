def nearest_words(lst, string):
    res = []
    length = len(string)
    for word in lst:
        if len(word) != length:
            continue
        one_wrong = 0
        for letter_index in range(length):
            if word[letter_index] == string[letter_index]:
                continue
            else:
                if one_wrong:
                    one_wrong = 2
                    break
                else:
                    one_wrong = 1
        if one_wrong != 2:
            res.append(word)
    return res


# print(nearest_words(['cats','snarf','carts','cat','bats','cbts','abcd'],'cats'))


def niven_numbers(n):
    res = []
    num = 1
    while len(res) < n:
        if num % sum([int(l) for l in str(num)]) == 0:
            if '9' in str(num):
                res.append(num)
        num += 1
    print(res)
