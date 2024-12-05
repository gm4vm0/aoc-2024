from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day

console = Console()


def part_one(input_data: list[str]):
    answer = 0

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(len(input_data)):
        for j in range(len(input_data[0])):
            if input_data[i][j] != "X":
                continue
            for direction in directions:
                delta_y = direction[0]
                delta_x = direction[1]

                if (
                    i + 3 * delta_y < 0
                    or i + 3 * delta_y >= len(input_data)
                    or j + 3 * delta_x < 0
                    or j + 3 * delta_x >= len(input_data[0])
                ):
                    continue

                if (
                    input_data[i + delta_y][j + delta_x] == "M"
                    and input_data[i + 2 * delta_y][j + 2 * delta_x] == "A"
                    and input_data[i + 3 * delta_y][j + 3 * delta_x] == "S"
                ):
                    answer += 1

    return answer


def part_two(input_data: list[str]):
    answer = 0

    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for i in range(1, len(input_data) - 1):
        for j in range(1, len(input_data[0]) - 1):
            if input_data[i][j] != "A":
                continue

            count = 0

            for direction in directions:
                m_y, m_x = (i + direction[0], j + direction[1])
                s_y, s_x = (i - direction[0], j - direction[1])

                if input_data[m_y][m_x] == "M" and input_data[s_y][s_x] == "S":
                    count += 1

            answer += count == 2

    return answer


def main():
    data = get_input_for_day(4)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
