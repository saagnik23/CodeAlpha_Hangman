import random


def display_hangman(wrong_guesses):
    """Display the hangman based on number of wrong guesses"""
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[wrong_guesses]


def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    """Main game function"""
    # List of words to choose from
    words = ["python", "computer", "programming", "keyboard", "developer", "codealpha", "nxtwave", "microsoft", "apple"]

    # Select a random word
    word = random.choice(words).lower()

    # Game variables
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("=== HANGMAN GAME ===")
    print(f"Guess the word! You have {max_wrong} incorrect guesses allowed.\n")

    # Main game loop
    while wrong_guesses < max_wrong:
        # Display current state
        print(display_hangman(wrong_guesses))
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Wrong guesses remaining: {max_wrong - wrong_guesses}")

        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You won! The word was '{word}'")
            break

        # Get player input
        guess = input("\nGuess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        # Add guess to list
        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in word:
            print(f"✓ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"✗ Sorry, '{guess}' is not in the word.")

    # Game over - player lost
    if wrong_guesses == max_wrong:
        print(display_hangman(wrong_guesses))
        print(f"\n💀 Game Over! The word was '{word}'")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        print("\n" + "=" * 50 + "\n")
        play_hangman()
    else:
        print("Thanks for playing!")


# Start the game
if __name__ == "__main__":
    play_hangman()