import urllib.request
import ssl
url = "https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt"


def read_input_file(url, number):
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url
    
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    website = open()
    with open(urllib.request.urlopen(url), "w", encoding="utf-8") as website:
        res = []
        for line in website:
            
            if len(res) == number:
                break
            x = line.decode("utf-8").strip().split()
            try:
                index = int(x[0])
                ans = []
                name = " ".join((x[1], x[2], x[3]))
                to_append = [x[0], name]
                ans.append(x[0])
                ans.append(name)
                ans.append("+")
                ans.append(x[6])
            except ValueError as identifier:
                pass
            if x[0] == 'Середній':
                ans.append(x[-1])
                res.append(ans)
    return res


read_input_file(url, 3)


def write_csv_file(url):
    to_write = read_input_file(url, 50)
    res = []
    for i in range(len(to_write)):
        res.append(",".join(to_write[i]))
    to_write = "\n".join(res)
    print(to_write)
    with open('topics.txt', 'w') as output_file:
        output_file.write("1,Мацюк М. І.")


write_csv_file(url)
# import doctest
# doctest.testmod()
