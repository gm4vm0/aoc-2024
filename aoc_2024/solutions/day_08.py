from rich.console import Console
from rich.pretty import pprint

from aoc_2024.utils.get_input_for_day import get_input_for_day

console = Console()


def part_one(input_data: list[str]):
    height, width = len(input_data), len(input_data[0])
    antennas_map = {}
    antinodes = set()

    for i in range(height):
        for j in range(width):
            if input_data[i][j] != ".":
                antennas_map.setdefault(input_data[i][j], []).append((i, j))

    for antennas in antennas_map.values():
        for i in range(len(antennas) - 1):
            for j in range(i + 1, len(antennas)):
                cur_y, cur_x, other_y, other_x = (
                    antennas[i][0],
                    antennas[i][1],
                    antennas[j][0],
                    antennas[j][1],
                )
                delta_y = other_y - cur_y
                delta_x = other_x - cur_x
                if 0 <= cur_y - delta_y < height and 0 <= cur_x - delta_x < width:
                    antinodes.add((cur_y - delta_y, cur_x - delta_x))
                if 0 <= other_y + delta_y < height and 0 <= other_x + delta_x < width:
                    antinodes.add((other_y + delta_y, other_x + delta_x))

    return len(antinodes)


def part_two(input_data: list[str]):
    height, width = len(input_data), len(input_data[0])
    antennas_map = {}
    antinodes = set()

    for i in range(height):
        for j in range(width):
            if input_data[i][j] != ".":
                antennas_map.setdefault(input_data[i][j], []).append((i, j))

    for antennas in antennas_map.values():
        for i in range(len(antennas) - 1):
            for j in range(i + 1, len(antennas)):
                cur_y, cur_x, other_y, other_x = (
                    antennas[i][0],
                    antennas[i][1],
                    antennas[j][0],
                    antennas[j][1],
                )
                delta_y = other_y - cur_y
                delta_x = other_x - cur_x
                next_y, next_x = cur_y, cur_x
                while 0 <= next_y < height and 0 <= next_x < width:
                    antinodes.add((next_y, next_x))
                    next_y -= delta_y
                    next_x -= delta_x
                next_y, next_x = cur_y + delta_y, cur_x + delta_x
                while 0 <= next_y < height and 0 <= next_x < width:
                    antinodes.add((next_y, next_x))
                    next_y += delta_y
                    next_x += delta_x

    return len(antinodes)


def main():
    data = get_input_for_day(8)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part two: {part_two_answer}")


if __name__ == "__main__":
    main()
