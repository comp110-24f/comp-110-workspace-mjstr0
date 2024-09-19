"""A program that counts the number of times a character appears in a given phrase."""

__author__ = "730552119"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0

    while index < len(
        phrase
    ):  # while loop continues up until the last index of the phrase
        if (
            phrase[index] == search_char
        ):  # checks if current index position is equal to search_char
            count += 1  #
        index += 1

    return count
