import unittest
from aoc_2024.solutions.day_03 import part_one, part_two


class Test(unittest.TestCase):
    def test_part_one(self):
        test_input = [
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        ]
        self.assertEqual(part_one(test_input), 161)

    def test_part_two(self):
        test_input = [
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        ]
        self.assertEqual(part_two(test_input), 48)


def main():
    unittest.main()
