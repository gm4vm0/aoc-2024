from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day

console = Console()


def part_one(input_data: list[str]):
    answer = 0

    def is_possible(value: int, operands: list[int], cur: int):
        if cur == value:
            return True
        if len(operands) == 0:
            return False
        return is_possible(value, operands[1:], cur + operands[0]) or is_possible(
            value, operands[1:], cur * operands[0]
        )

    for equation in input_data:
        value, operands = equation.split(": ")
        value = int(value)
        operands = list(map(int, operands.split()))
        answer += is_possible(value, operands[1:], operands[0]) * value

    return answer


def part_two(input_data: list[str]):
    answer = ...

    return answer


def main():
    data = get_input_for_day(7)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
