import random

# Step 1: Define the word list
word_list = ["apple", "tiger", "chair", "water", "plane"]

# Step 2: Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Step 3: Set up game state
guessed_word = ["_"] * word_length
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

# Step 4: Game loop
while attempts_left > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                guessed_word[index] = guess
        print("Good guess:", " ".join(guessed_word))
    else:
        attempts_left -= 1
        print(f"Wrong guess! You have {attempts_left} attempts left.")
        print("Current word:", " ".join(guessed_word))

# Step 5: End of game
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
