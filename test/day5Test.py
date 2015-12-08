from unittest import TestCase
from src.Day5 import Day5


class Day5Test(TestCase):
    def setUp(self):
        self.day = Day5()

    def tearDown(self):
        pass

    def test_vowels(self):
        keys = ['aeidd']
        self.assertEqual(1, self.day.nice(keys))
        keys = ['xazegovdd']
        self.assertEqual(1, self.day.nice(keys))
        keys = ['aeiouaeiouaeioudd']
        self.assertEqual(1, self.day.nice(keys))

    def test_double_letter(self):
        keys = ['aeiddf']
        self.assertEqual(1, self.day.nice(keys))

    def test_complex(self):
        keys = ['ugknbfddgicrmopn']
        self.assertEqual(1, self.day.nice(keys))
        keys = ['aaa']
        self.assertEqual(1, self.day.nice(keys))
        keys = ['jchzalrnumimnmhp']  # naughty because it has no double letter.
        self.assertEqual(0, self.day.nice(keys))
        keys = ['haegwjzuvuyypxyu']  # naughty because it contains the string xy.
        self.assertEqual(0, self.day.nice(keys))
        keys = ['dvszwmarrgswjxmb']  # naughty because it contains only one vowel.
        self.assertEqual(0, self.day.nice(keys))

    def test_nice(self):
        strings = ['qjhvhtzxzqqjkmpb']
        self.assertEqual(1, self.day.niceToo(strings))
        strings = ['xxyxx']
        self.assertEqual(1, self.day.niceToo(strings))
        strings = ['uurcxstgmygtbstg']
        self.assertEqual(0, self.day.niceToo(strings))
        strings = ['ieodomkazucvgmuy']
        self.assertEqual(0, self.day.niceToo(strings))

    def test_demarde(self):
        strings = ['rxexcbwhiywwwwnu']
        self.assertEqual(1, self.day.niceToo(strings))

