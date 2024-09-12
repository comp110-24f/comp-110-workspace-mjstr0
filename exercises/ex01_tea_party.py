"""Planning for a tea party!"""

__author__: str = "730552119"


def main_planner(guests: int) -> None:
    "calls each fucntion and produces printed output"
    # use print function to print each output

    print(
        "A Cozy Tea Party for " + str(guests) + " people!"
    )  # use str so that we can concatenate an integer

    print(
        "Tea Bags: " + str(tea_bags(guests))
    )  # add space after colon for better formatting

    print("Treats: " + str(treats(guests)))

    print(
        "Cost: $"
        + str(
            cost(tea_bags(guests), treats(guests))
        )  # call on tea_bags and treats function using guests as the parameter
    )  # to include $ sign in output

    return None  # optional as will return None by default


def tea_bags(people: int) -> int:
    "Calculates the number of tea bags needed based on number of guests"
    return people * 2  # assuming each guests will drink two cups of tea


def treats(people: int) -> int:
    "Calculates number of treats needed based on the number of teas guests are expecting to drink"
    return int(
        tea_bags(people=people) * 1.5  # assuming for each tea 1.5 treats are needed
    )  # using people as a keyword argument to call on tea_bags function # using int changes output from a float to an integer


def cost(tea_count: int, treat_count: int) -> float:
    "compute the cost of the tea bags and the treats combined"
    return tea_count * 0.5 + treat_count * 0.75
    # tea bag costs $0.50 and each treat costs $0.75 # count times unit price ($)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
