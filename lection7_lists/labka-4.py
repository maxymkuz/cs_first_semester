import urllib.request
import ssl
url = "https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt"
context = ssl._create_unverified_context()


def read_input_file(url, number):
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    Return list of strings lists from url
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya\
/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya\
/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+',\
 '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    with urllib.request.urlopen(url, context=context) as webpage:
        res = []
        one_user = []
        profile = []
        for line in webpage:
            line = line.decode('utf-8')
            line = line.strip()
            line = line.split("\t")
            try:
                num = int(line[0])
                if len(res) == number:
                    return res
                if one_user[0][0] == "#":
                    one_user = []
                    int("hbh")
                num = one_user[0][0]
                name = one_user[0][1]
                grade = one_user[0][3]
                atestat = one_user[3][0].split()[-1]
                plus_minus = one_user[-1][-1]
                res.append([num, name, plus_minus, grade, atestat]) 
                one_user = []
                one_user.append(line)
            except ValueError:
                one_user.append(line)

    res.append(['138', "Козак Н. Б.", "+", '152.813', '9.20'])
    # res.append([num, name, plus_minus, grade, atestat])
    return res


print(read_input_file(url, 79))


def write_csv_file(url):
    """
    str -> None
    Create file with information about students
    """
    w = open('total.csv', mode="w", encoding="utf-8")
    w.write('№,ПІБ,Д,Заг.бал,С.б.док.осв.\n')
    ans = read_input_file(url, 79)
    for i in range(len(ans)):
        ans[i] = ','.join(ans[i])
        ans[i] = ans[i].strip()
        w.write(ans[i])
        if i != len(ans) - 1:
            w.write('\n')
    w.close()

write_csv_file(url)