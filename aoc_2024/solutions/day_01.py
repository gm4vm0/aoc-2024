from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day


def part_one(input_data: list[str]):
    answer = 0

    left_list = []
    right_list = []

    for line in input_data:
        left, right = line.split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list = sorted(left_list)
    right_list = sorted(right_list)

    for i in range(len(input_data)):
        answer += abs(left_list[i] - right_list[i])

    return answer


def part_two(input_data: list[str]):
    answer = ...

    return answer


def main():
    console = Console()
    data = get_input_for_day(1)

    console.status("Computing answer for part 1...", spinner="christmas")
    part_one_answer = part_one(data)
    console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    console.status("Computing answer for part 2...", spinner="christmas")
    part_two_answer = part_two(data)
    console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
