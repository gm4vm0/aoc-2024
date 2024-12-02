from argparse import ArgumentParser
import unittest

from rich.console import Console


console = Console()


def main():
    """
    Runs test script for specified day
    """
    day = _parse_args()

    try:
        module = f"tests.aoc_2024.solutions.test_day_{day:02}"
        unittest.main(module=module, argv=["unittest"])
    except ImportError:
        console.log("[red]Test script not found")


def _parse_args() -> int:
    """
    Parse command line arguments
    """
    parser = ArgumentParser(description="Run test script for specified day")
    parser.add_argument("day", type=int, help="Day to run test for")
    args = parser.parse_args()
    return args.day


if __name__ == "__main__":
    main()
