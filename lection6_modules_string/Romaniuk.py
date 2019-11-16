str_1 = '12345678910'
str_2 = 'abcd'


def string_merge(str1, str2):
    str_res = ""
    """
    (str, str) -> str
    """

    for i in zip(str1, str2):
        str_res += i[0] + i[1]

    return str_res


if __name__ == "__main__":
    print(string_merge(str_1, str_2))
    print("i'm here")