import string


def characters_info(path):
    lines = []
    min_length = 10**5
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if len(line) < min_length:
                min_length = len(line)
            lines.append(line)
    to_write = ""
    for i in range(min_length):
        temp = [word[i] for word in lines]
        unique = [x for x in temp if x in "bcdfghjklmnpqrstvwxz"]
        for j in range(len(temp)):
            to_write += temp[j]
        for j in range(len(unique)):
            to_write += unique[j]
        to_write += "\n"
    print(to_write)
    f = open("text_1.txt", "w", encoding="utf-8")
    f.write(to_write)
