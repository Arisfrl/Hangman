import random
import os
import hangman_art


# function to find all the occurrences the given letter
def find_indexes(word, character):
    indexes = []
    for i in range(len(word)):
        if word[i] == character:
            indexes.append(i)
    return indexes


# function to replace all the occurrences the given letter in the blank word.
def replace_letter(word, character, indexes):
    for index in indexes:
        word[index] = character
    return word


random_words = ["Apple", "Banana", "Cat", "Dog", "Else", "Future", "Gold", "Hydrogen", "Island", "January"]
max_life = 6

random_word = list(random.choice(random_words).lower())
blank_word = list('_' * len(random_word))

# print(random_word, blank_word)
while max_life > 0:
    hangman_art.display_logo()
    hangman_art.display_life(max_life)
    print(' '.join(map(str, blank_word)))
    letter = input("Guess a letter: ").lower()
    os.system('cls')
    if letter in blank_word or letter not in random_word:
        max_life -= 1
        if letter in blank_word:
            print('You have already guessed that letter. Choose again.')
        else:
            print("Ops, No such letter in our word")

    else:
        occurrences = find_indexes(random_word, letter)
        blank_word = replace_letter(blank_word, letter, occurrences)
        if "_" not in blank_word:
            hangman_art.display_logo()
            hangman_art.display_life(max_life)
            print(' '.join(map(str, blank_word)))
            print("Congrats, you guess it right.")
            print("  0   ")
            print("~~|~~ ")
            print(" / \  ")
            print("You just saved me!")
            print("You won!")
            break
        else:
            continue

if max_life == 0:
    os.system('cls')
    hangman_art.display_logo()
    hangman_art.display_life(max_life)