from words import get_word
from image import hangman_image


def show_random_word(word: str, guessed_letters: set) -> str:
    return "".join(letter if letter in guessed_letters else "_" for letter in word)


def input_validation() -> str:
    while True:
        guess = input("Guess a letter or word: ").lower()
        if guess.isalpha():
            return guess
        print("Invalid input. Please enter letters only.")


def evaluate_guess(guess: str, word: str, guessed_letters: set, mistakes: int) -> int:
    if len(guess) == 1:
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            guessed_letters.add(guess)
            mistakes += 1
            print("Wrong guess!")
    else:
        if guess == word:
            print("Congratulations! You win!")
            return -1
        else:
            mistakes += 1
            print("Wrong guess!")

    return mistakes


def play_hangman_game(word: str, max_attempts: int = 10, max_mistakes: int = 6) -> None:
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Hangman game!")
    print(show_random_word(word, guessed_letters))

    while mistakes < max_mistakes and len(guessed_letters) < max_attempts:
        guess = input_validation()
        mistakes = evaluate_guess(guess, word, guessed_letters, mistakes)

        if mistakes == -1:
            return

        print(show_random_word(word, guessed_letters))
        hangman_image(mistakes)

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You win!")
            return

        print("Mistakes left:", max_mistakes - mistakes)
        print("Attempts left:", max_attempts - len(guessed_letters))
        print("Guessed letters:", ",".join(guessed_letters))

    print("Game over! The word was:", word)


if __name__ == "__main__":
    word = get_word()
    play_hangman_game(word)
