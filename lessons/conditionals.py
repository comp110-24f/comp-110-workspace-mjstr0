""""Practice with conditionals"""


def check_first_letter(word: str, letter: str) -> str:
    "return “match!” if the first character of word is letter"

    if word[0] == letter:
        return "match!"
    else:
        return "no match"

    print(check_first_letter("happy", "h"))
