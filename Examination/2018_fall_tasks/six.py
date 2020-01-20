import string

if __name__ == "__main__":
    inpt = input("Enter string: ")
    line = ""
    for symbol in inpt:
        if symbol in string.ascii_letters:
            if symbol.isupper():
                line += symbol.lower()
            else:
                line += symbol.upper()
    print(line)
