import unittest
from aoc_2024.solutions.day_07 import part_one, part_two


test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".split(
    "\n"
)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 3749)

    def test_part_two(self):
        self.assertEqual(part_two(test_input), 11387)


def main():
    unittest.main()
