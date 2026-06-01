import random

word_list = [
    "python",
    "laptop",
    "coding",
    "school",
    "planet"
]

selected_word = random.choice(word_list)

guessed_letters = []

remaining_attempts = 6

print("===== HANGMAN GAME =====")
print("Guess the hidden word")

while remaining_attempts > 0:

    display_word = ""

    for letter in selected_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly.")
        break

    user_letter = input("Enter a letter: ").lower()

    if len(user_letter) != 1:
        print("Please enter only one letter.")
        continue

    if user_letter in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(user_letter)

    if user_letter in selected_word:
        print("Correct Guess!")
    else:
        remaining_attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts:", remaining_attempts)

if remaining_attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", selected_word)