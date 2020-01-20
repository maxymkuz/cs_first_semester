def characters_info(path):
    vovels = "eioau"
    to_write = ""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            answers = [[letter, 0] for letter in vovels]

            for symbol in line:
                to_write += symbol
                if symbol in vovels:
                    for i in range(len(answers)):
                        if answers[i][0] == symbol:
                            answers[i][1] += 1
            answers.sort(key=lambda x: x[0])
            answers.sort(key=lambda x: x[1])

            for i in range(len(answers)):
                if answers[i][1] != 0:
                    to_write += answers[i][0]
            print(answers)
            to_write += "\n"

    with open("text_1.txt", "w", encoding="utf-8") as file:
        file.write(to_write)


characters_info("text.txt")
