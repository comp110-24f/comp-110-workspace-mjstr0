def get_weather_report() -> str:
    """display weather"""
    weather: str = input(
        "What is the weather?"
    )  # input function displays the question to the user
    if (
        weather == "rainy" or weather == "cold"
    ):  # so that rainy and cold is both evaluated, otherwsie or just separest the two
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I dont recognize this weather.")
    return weather


get_weather_report()
