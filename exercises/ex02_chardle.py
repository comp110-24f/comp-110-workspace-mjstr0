"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "1234567890"


def input_word() -> str:
    """Gathers an input from the user."""
    word: str = input("Enter a 5-character word: ")  # prompts the user to enter a word
    if len(word) != 5:  # so that if len = 5 the word is returned
        print("Error: Word must contain 5 characters.")  # include "Error" in message
        exit()  # place exit here, if word is not 5 characters program will quit
    return word


def input_letter() -> str:
    """Gathers a single character from the user"""
    letter: str = input(
        "Enter a single character: "
    )  # prompts the user to enter a character
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()  # place exit here, if input is not a single character program will quit
    return letter


def contains_char(word: str, letter: str) -> None:
    """Checks if the letter is present in the word and at what index it is found."""
    print("Searching for " + letter + " in " + word)  # to concatenate use +
    count: int = 0

    if (
        word[0] == letter
    ):  # index to check if letter is found at a certain place in the word
        print(letter + " found at index 0")
        count += 1  # add 1 count everytime the letter appears in the word
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    if count == 0:  # counts number of instances, either 0, 1 or greater than 1
        print(
            "No instances of " + letter + " found in " + word
        )  # make sure of spacing for correct formatting
    elif count == 1:
        print(
            "1 instance of " + letter + " found in " + word
        )  # so that instance is singular
    else:
        print(str(count) + " instances of " + letter + " found in " + word)  # count > 1


def main() -> None:
    """Coordinates the flow of the game by calling other functions."""
    word = input_word()  # call each function that has been defined
    letter = input_letter()
    contains_char(word, letter)


if __name__ == "__main__":
    main()
