import unittest
from aoc_2024.solutions.day_06 import part_one, part_two


test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".split(
    "\n"
)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 41)

    @unittest.skip("Not yet implemented")
    def test_part_two(self):
        self.assertEqual(part_two(test_input), "x")


def main():
    unittest.main()
