import unittest
from aoc_2024.solutions.day_02 import part_one, part_two


test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split(
    "\n"
)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 2)

    @unittest.skip("Not yet implemented")
    def test_part_two(self):
        self.assertEqual(part_two(test_input), "x")


def main():
    unittest.main()
