import os

from dotenv import load_dotenv
from requests import get


def get_input(day: int):
    load_dotenv()
    session = os.environ["AOC_SESSION"]
    data = _download_input(day, session)
    _save_input(data, day)


def _download_input(day: int, session: str) -> bytes:
    """
    Downloads the input as text from the AOC site
    """
    cookies = {"session": session}
    url = f"https://adventofcode.com/2024/day/{day}/input"
    resp = get(url, cookies=cookies)
    resp.raise_for_status()
    return resp.content


def _save_input(data: bytes, day: int) -> None:
    with open(os.path.join("aoc_2024", "inputs", f"day_{day:02}.txt"), "wb") as file:
        file.write(data)
