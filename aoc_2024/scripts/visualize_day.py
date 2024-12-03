from argparse import ArgumentParser
import importlib

from rich.console import Console


console = Console()


def main():
    """
    Runs solution script for specified day
    """
    day = _parse_args()

    try:
        module = importlib.import_module(f"aoc_2024.visualizations.day_{day:02}")
        module.main()
    except ModuleNotFoundError:
        console.log("[red]Visualization script not found")


def _parse_args() -> int:
    """
    Parse command line arguments
    """
    parser = ArgumentParser(description="Run visualization script for specified day")
    parser.add_argument("day", type=int, help="Day to run visualization for")
    args = parser.parse_args()
    return args.day


if __name__ == "__main__":
    main()
