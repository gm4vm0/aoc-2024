from time import sleep
from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day


def part_one(input_data: list[str]):
    answer = 0

    for report in input_data:
        levels = report.split()
        if levels[0] == levels[1]:
            continue
        isIncreasing = int(levels[0]) < int(levels[1])
        isSafe = True
        for i in range(1, len(levels)):
            diff = int(levels[i]) - int(levels[i - 1])
            if isIncreasing and diff < 1 or diff > 3:
                isSafe = False
            elif not isIncreasing and diff > -1 or diff < -3:
                isSafe = False
        answer += isSafe

    return answer


def part_two(input_data: list[str]):
    answer = ...

    return answer


def main():
    console = Console()
    data = get_input_for_day(2)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
