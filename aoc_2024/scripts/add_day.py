from argparse import ArgumentParser
import os

from rich.console import Console

from aoc_2024.scripts.get_input import get_input
from aoc_2024.utils.get_input_for_day import get_input_for_day


console = Console()


def main():
    """
    Creates template files for specified day and download input from the AOC website.
    """
    day = _parse_args()

    console.log(
        f"[bold green]:christmas_tree: Generating template files and downloading input data for day {day}..."
    )
    _create_solution_template(day)
    _create_test_template(day)
    _download_input(day)


def _parse_args() -> int:
    """
    Parse command line arguments
    """
    parser = ArgumentParser(description="Add a day to generate template files")
    parser.add_argument("day", type=int, help="Day to generate template for")
    args = parser.parse_args()
    return args.day


def _create_solution_template(day: int) -> None:
    """
    Copies solution template to target day directory

    Args:
        day (int): day to generate template for
    """
    with open("aoc_2024/scripts/templates/solution_template.txt") as f:
        template = f.read()
    template = template.replace("{day}", str(day))
    solution_module_path = os.path.join("aoc_2024", f"solutions")
    solution_file_path = os.path.join(solution_module_path, f"day_{day:02}.py")
    if os.path.exists(solution_file_path):
        console.log(
            f"[yellow]File [italic]{solution_file_path}[/italic] already exists"
        )
        return
    else:
        with open(solution_file_path, "w") as f:
            f.write(template)
        console.bell()
        console.log(
            f"[green]Solution template written to [italic]{solution_file_path}[/italic]"
        )


def _create_test_template(day: int) -> None:
    """
    Copies test template to target day directory

    Args:
        day (int): day to generate template for
    """
    with open("aoc_2024/scripts/templates/test_template.txt") as f:
        template = f.read()
    template = template.replace("{file_day}", f"{day:02}")
    test_module_path = os.path.join("tests", "aoc_2024", "solutions")
    test_file_path = os.path.join(test_module_path, f"test_day_{day:02}.py")
    if os.path.exists(test_file_path):
        console.log(f"[yellow]File [italic]{test_file_path}[/italic] already exists")
        return
    else:
        with open(test_file_path, "w") as f:
            f.write(template)
        console.bell()
        console.log(
            f"[green]Test template written to [italic]{test_file_path}[/italic]"
        )


def _download_input(day: int) -> None:
    input_data_path = os.path.join("aoc_2024", "inputs", f"day_{day:02}.txt")
    try:
        _ = get_input_for_day(day)
        console.log(f"[yellow]File [italic]{input_data_path}[/italic] already exists")
        return
    except FileNotFoundError:
        try:
            get_input(day)
            console.log(
                f"[green]Input data downloaded to [italic]{input_data_path}[/italic]"
            )
            return
        except Exception as e:
            console.log(f"[red]Could not retrieve input data:\n\t{e}")
            return
