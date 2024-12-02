import unittest
from aoc_2024.solutions.day_01 import part_one, part_two


test_input = """3   4
4   3
2   5
1   3
3   9
3   3""".split(
    "\n"
)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 11)

    @unittest.skip("Not yet implemented")
    def test_part_two(self):
        self.assertEqual(part_two(test_input), "x")


def main():
    unittest.main()
