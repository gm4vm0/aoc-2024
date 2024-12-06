from rich.console import Console

from aoc_2024.utils.get_input_for_day import get_input_for_day

console = Console()


def part_one(input_data: list[str]):
    answer = 1

    directions = {
        # (dir_y, dir_x, next_dir)
        "^": (-1, 0, ">"),
        ">": (0, 1, "v"),
        "v": (1, 0, "<"),
        "<": (0, -1, "^"),
    }

    cur_loc = (0, 0)
    cur_dir = ""
    for i in range(len(input_data)):
        input_data[i] = list(input_data[i])
        for j in range(len(input_data[0])):
            if input_data[i][j] in directions:
                cur_loc = (i, j)
                cur_dir = input_data[i][j]
                break

    cur_y, cur_x = cur_loc

    while True:
        next_y, next_x = cur_y + directions[cur_dir][0], cur_x + directions[cur_dir][1]

        if not (0 <= next_y < len(input_data) and 0 <= next_x < len(input_data[0])):
            break

        if input_data[next_y][next_x] == "#":
            input_data[cur_y][cur_x] = cur_dir = directions[cur_dir][2]
        else:
            input_data[cur_y][cur_x] = "X"
            cur_y, cur_x = next_y, next_x
            answer += input_data[cur_y][cur_x] == "."
            input_data[cur_y][cur_x] = cur_dir

    return answer


def part_two(input_data: list[str]):
    answer = ...

    return answer


def main():
    data = get_input_for_day(6)

    with console.status("Computing answer for part 1...", spinner="christmas"):
        part_one_answer = part_one(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_one_answer}")

    with console.status("Computing answer for part 2...", spinner="christmas"):
        part_two_answer = part_two(data)
        console.print(f"[bold]:snowman: Answer to part one: {part_two_answer}")


if __name__ == "__main__":
    main()
