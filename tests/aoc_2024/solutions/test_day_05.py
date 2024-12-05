import unittest
from aoc_2024.solutions.day_05 import part_one, part_two


test_input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".split(
    "\n"
)


class Test(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one(test_input), 143)

    @unittest.skip("Not yet implemented")
    def test_part_two(self):
        self.assertEqual(part_two(test_input), "x")


def main():
    unittest.main()
