import unittest
from aoc_2024.solutions.day_04 import part_one, part_two


test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split(
    "\n"
)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 18)

    @unittest.skip("Not yet implemented")
    def test_part_two(self):
        self.assertEqual(part_two(test_input), "x")


def main():
    unittest.main()
