def reverse_word(word):
    res = ""
    for letter in range(len(word) - 1, -1, -1):
        res += word[letter]
    return res


if __name__ == "__main__":
    inpt = input("Enter yout sentence: ")

    string = ""
    for symbol in inpt:
        if symbol not in ":.,;-!?":
            string += symbol.lower()

    res = [word for word in string.split() if word == reverse_word(word)]

    print(" ".join(res))
