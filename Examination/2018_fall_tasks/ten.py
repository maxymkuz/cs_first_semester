def main(A, B):
    if A == B:
        print(A)
    elif B < A:
        print(B)
        main(A, B + 1)
    elif A < B:
        print(A)
        main(A + 1, B)


main(8, 15)
