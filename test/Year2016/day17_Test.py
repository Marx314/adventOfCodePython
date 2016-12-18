from unittest import TestCase
import unittest

from src.Year2016.Day17 import OPEN, CLOSED, Day17


class Day17Test(TestCase):
    def setUp(self):
        self.day = Day17()

    def test_basic(self):
        self.assertEqual(self.day.first_four_from_md5('hijkl'), 'ced9')
        self.assertEqual(self.day.generate_move('ced9'), {'UP': OPEN, 'DOWN': OPEN, 'LEFT': OPEN, 'RIGHT': CLOSED})

    def test_simple(self):
        position = ((0, 0), 'ihgpwlah')
        self.assertEqual(self.day.calculate_path(position), 'DDRRRD')
        position = ((0, 0), 'kglvqrro')
        self.assertEqual(self.day.calculate_path(position), 'DDUDRLRRUDRD')
        position = ((0, 0), 'ulqzkmiv')
        self.assertEqual(self.day.calculate_path(position), 'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

    def test_puzzle(self):
        position = ((0, 0), self.puzzle())
        self.assertEqual(self.day.calculate_path(position), 'RDRRULDDDR')

    @unittest.skip('test case are more complex then puzzle itself')
    def test_simple_part2(self):
        position = ((0, 0), 'ihgpwlah')
        self.assertEqual(self.day.calculate_longest_path(position), 370)
        position = ((0, 0), 'kglvqrro')
        self.assertEqual(self.day.calculate_longest_path(position), 492)
        position = ((0, 0), 'ulqzkmiv')
        self.assertEqual(self.day.calculate_longest_path(position), 830)

    def test_puzzle_part2(self):
        position = ((0, 0), self.puzzle())
        self.assertEqual(self.day.calculate_longest_path(position), 392)

    def puzzle(self):
        return '''vkjiggvb'''
