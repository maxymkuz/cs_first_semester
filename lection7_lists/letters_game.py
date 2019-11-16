letters = ["a", "b", "c", "d", "g", "o", "s", "t"]
counter = 0
all_words = []
f = open("en.txt")


word_is_ok = False
for word in f:
    word = word.strip()
    word_is_ok = True

    for letter in word:
        if letter not in letters:
            word_is_ok = False
            break
    if word_is_ok:
        all_words.append(word)

# print(all_words)
f.close()

while True:
    user_input = input()
    wrong_word = False
    used_words = [False] * len(letters)   
    if user_input == 'q':
        break

    # checking if input contains only letters
    for letter in user_input:
        if letter not in letters:
            wrong_word = True

    if wrong_word:
        print('wrong letter')
        continue

    correct = False

    f = open("en.txt")
    for word in f:
        word = word.strip()
        if word == user_input:
            counter += 1
            print("right!!!!!!!!")
            correct = True

            break
    
    if not correct:
        print("wrong here")

print("guessed", counter)
print("total", len(all_words))