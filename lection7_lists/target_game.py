import random


def generate_grid():
    """
    () -> list(list)

    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    return [[chr(random.randint(65, 90)) for j in range(3)] for i in range(3)]


def get_words(f, letters):
    """
    (str, list) -> list

    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, encoding="utf-8") as file:
        list_letter = []
        res = []


        if len(letters) <= 3:
            for i in range(3):
                for j in range(3):
                    list_letter.append(letters[i][j].lower())



        else:
            list_letter = letters
        for word in file:
            word = word.strip().lower()
            word_is_ok = True
            checker = 9*[True]
            
            if len(word) < 4:
                continue
            for letter in word:


                letter_not_in = True  
                for i in range(9):
                    if letter == list_letter[i] and checker[i]:
                        checker[i] = False
                        letter_not_in = False
                        break


                    
                if letter_not_in or list_letter[4] not in word:
                    word_is_ok = False
                    break

            if word_is_ok:
                res.append(word)
        if len(set(res)) == 0:  # if there's no words from our arr
            res = get_words(f, generate_grid())
        return res




def get_user_words():
    """
    () -> list

    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    res = []
    print("here")
    while True:
        try:
            inpt = input()
            res.append(inpt)
        except KeyboardInterrupt:
            break
    return res


def get_pure_user_words(user_words, letters, words_from_dict):
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    list_letter = []
    res = []
    if len(letters) <= 3:
        for i in range(3):
            for j in range(3):
                list_letter.append(letters[i][j].lower())
    else:
        list_letter = letters

    for word in user_words:
        word = word.strip().lower()
        word_is_ok = True
        checker = 9*[True]
        if len(word) < 4:
            continue
        for letter in word:
            letter_not_in = True
            for i in range(9):
                if letter == list_letter[i] and checker[i]:
                    checker[i] = False
                    letter_not_in = False
                    break
            if letter_not_in or list_letter[4] not in word:
                word_is_ok = False
                break

        if word_is_ok:
            if word not in words_from_dict:
                res.append(word)

    return res


def results():
    """
    None -> None
    writes the number of right words,all possible words, words that user didn't 
    guess and pure words that user invented into a file
    """
    guessed = []
    missed_words = []
    res = []
    letters = generate_grid()
    words_from_dict = get_words("en.txt", letters)
    print(words_from_dict)
    user_words = get_user_words()
    print(user_words)
    for word in words_from_dict:
        if word in user_words:
            guessed.append(word)
        else:
            missed_words.append(word)
    print(guessed, missed_words)
    pure = get_pure_user_words(user_words, letters, words_from_dict)
    res.append(len(guessed))
    res.append(words_from_dict)
    res.append(missed_words)
    res.append(pure)
    with open('result.txt', 'w') as output_file:
        output_file.write(str(res))

results()
