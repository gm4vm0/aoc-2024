import re

from rich.console import Console
from aoc_2024.utils.get_input_for_day import get_input_for_day

console = Console()


def part_one(input_data: list[str]):
    answer = 0

    memory = "".join(input_data)

    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    match = pattern.search(memory)
    while match:
        instruction = match.group()
        match = pattern.search(memory, match.end())
        digit = re.compile(r"\d+")
        first = digit.search(instruction)
        second = digit.search(instruction, first.end())
        answer += int(first.group()) * int(second.group())

    return answer


def part_two(input_data: list[str]):
    answer = ...

    return answer


def main():
    data = get_input_for_day(3)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
