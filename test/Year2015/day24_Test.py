from unittest import TestCase
import unittest

from src.Year2015.Day24 import Day24


class Day24Test(TestCase):
    def setUp(self):
        self.day = Day24()

    def test_simple(self):
        p = list(range(1, 6)) + list(range(7, 12))
        first_qe = self.day.get_first_quantum_entanglement(p)
        self.assertEqual(first_qe, 99)

    @unittest.skip('TLDR')
    def test_puzzle(self):
        qe = self.day.get_first_quantum_entanglement(self.day.make_list(self.puzzle()))
        self.assertEqual(qe, 11846773891)

    def test_puzzle_part2(self):
        qe = self.day.get_first_quantum_entanglement(self.day.make_list(self.puzzle()), 4)
        self.assertEqual(qe, 80393059)

    def test_make_list_work(self):
        r = self.day.make_list(self.puzzle())
        self.assertEqual(r[0], 1)
        self.assertEqual(r[2], 3)
        self.assertEqual(r[-1], 113)

    def puzzle(self):
        return '''1
2
3
7
11
13
17
19
23
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113'''
