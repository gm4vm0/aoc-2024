from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day


def part_one(input_data: list[str]):
    answer = 0

    for report in input_data:
        levels = report.split()
        if levels[0] == levels[1]:
            continue
        is_increasing = int(levels[0]) < int(levels[1])
        is_safe = True
        for i in range(1, len(levels)):
            diff = int(levels[i]) - int(levels[i - 1])
            if is_increasing and diff < 1 or diff > 3:
                is_safe = False
            elif not is_increasing and diff > -1 or diff < -3:
                is_safe = False
        answer += is_safe

    return answer


def part_two(input_data: list[str]):
    answer = 0

    def check_safety(levels: list[str]) -> bool:
        if levels[0] == levels[1]:
            return False
        is_increasing = int(levels[0]) < int(levels[1])
        for i in range(1, len(levels)):
            diff = int(levels[i]) - int(levels[i - 1])
            if is_increasing and diff < 1 or diff > 3:
                return False
            elif not is_increasing and diff > -1 or diff < -3:
                return False
        return True

    for report in input_data:
        levels = report.split()
        is_safe = check_safety(levels)
        if not is_safe:
            for i in range(len(levels)):
                new_levels = levels.copy()
                new_levels.pop(i)
                is_safe = check_safety(new_levels)
                if is_safe:
                    break
        answer += is_safe

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
