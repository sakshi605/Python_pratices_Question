import random

# Step 1: Setup
word_list = ["apple", "beautiful", "potato"]
lives = 6
chosen_word = random.choice(word_list)
print("The word has", len(chosen_word), "letters.")

# Step 2: Display placeholder
display = []  # Start with an empty list
for letter in chosen_word:  # Go through each letter in the word
    display.append('-')     # Add a dash for each letter

print(" ".join(display))    # Show the dashes as a spaced string

game_over = False

# Step 3: Game loop
while not game_over:
    guess_letter = input("Guess a letter: ").lower()

    # Step 4: Check guessed letter
    if guess_letter in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess_letter:
                display[position] = guess_letter
    else:
        lives -= 1
        print(f"Wrong guess! Lives left: {lives}")
        if lives == 0:
            game_over = True
            print("You Lose!! The word was:", chosen_word)

    # Step 5: Show current progress
    print(" ".join(display))

    # Step 6: Win condition
    if '-' not in display:
        game_over = True
        print("You Win!! 🎉")
