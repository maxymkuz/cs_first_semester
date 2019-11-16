import time
import re

f = open('hello.txt', "r", encoding="utf-8")
# "r"--іменований(ключовий) аргумент
# windows-1251

start = time.time()
lines = []
# for line in f:
#     lines.append(line)
#     #print(line)
#     # 0.05485224723815918
# lines = f.readlines()  # 0.0249330997467041
symbols = [".", ",", "?", "!"]


def num_words():
    text = f.read()
    for sym in symbols:
        text = text.replace(sym, " ").lower()
    print(text)


num_words()
print(time.time() - start)

f.close()



