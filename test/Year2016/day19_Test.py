from unittest import TestCase

from src.Year2016.Day19 import Day19


class Day19Test(TestCase):
    def setUp(self):
        self.day = Day19()

    def test_simple(self):
        elf_count = 5

        self.assertEqual(self.day.get_elf_alive(elf_count), 3)

    def test_simple_part2(self):
        self.assertEqual(self.day.get_elf_alive_killing_the_one_facing(5), 2)

    def test_puzzle(self):
        self.assertEqual(self.day.get_elf_alive(self.puzzle()), 1834903)

    def test_puzzle_part2(self):
        self.assertEqual(self.day.get_elf_alive_killing_the_one_facing(self.puzzle()), 1420280)

    def puzzle(self):
        return 3014603
