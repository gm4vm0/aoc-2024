from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day

console = Console()


def part_one(input_data: list[str]):
    answer = 0

    line_num = 0
    rules = {}

    while input_data[line_num]:
        before, after = input_data[line_num].split("|")
        if after not in rules:
            rules[after] = []
        rules[after].append(before)
        line_num += 1

    line_num += 1

    while line_num < len(input_data):
        pages = input_data[line_num].split(",")
        forbidden = []
        is_correct = True
        for page in pages:
            if page in forbidden:
                is_correct = False
                break
            forbidden.extend(rules.get(page, []))
        answer += int(pages[len(pages) // 2]) if is_correct else 0
        line_num += 1

    return answer


def part_two(input_data: list[str]):
    answer = ...

    return answer


def main():
    data = get_input_for_day(5)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
