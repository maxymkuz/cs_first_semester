def main(X, Y):
    if X == Y:
        print(X)
    elif ord(X) < ord(Y):
        print(X)
        main(chr(ord(X) + 1), Y)
    else:
        print(X)
        main(chr(ord(X) - 1), Y)


main('y', 'a')