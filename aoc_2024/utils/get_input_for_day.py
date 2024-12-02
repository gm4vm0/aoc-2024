import os


def get_input_for_day(day: int) -> list[str]:
    """
    Get the input for the day as list of strings
    """
    input_file = os.path.join("aoc_2024", "inputs", f"day_{day:02}.txt")
    with open(input_file) as file:
        lines = file.readlines()
    return [line.rstrip() for line in lines]
