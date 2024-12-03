import unittest
from aoc_2024.solutions.day_03 import part_one, part_two


test_input = ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"]


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 161)

    @unittest.skip("Not yet implemented")
    def test_part_two(self):
        self.assertEqual(part_two(test_input), "x")


def main():
    unittest.main()
