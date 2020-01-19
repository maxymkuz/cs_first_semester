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