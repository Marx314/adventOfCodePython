from unittest import TestCase
from src.Day1 import Day1


class Day1Test(TestCase):
    def setUp(self):
        self.day = Day1()

    def tearDown(self):
        pass

    def test_first_scenario(self):
        datas = ['(())', '()()']
        for data in datas:
            self.assertEqual(0, self.day.calc(data))

    def test_second_scenario(self):
        datas = ['(((', '(()(()(', '))(((((']
        for data in datas:
            self.assertEqual(3, self.day.calc(data))

    def test_third_scenario(self):
        datas = ['())', '))(']
        for data in datas:
            self.assertEqual(-1, self.day.calc(data))

    def test_forth_scenario(self):
        datas = [')))', ')())())']
        for data in datas:
            self.assertEqual(-3, self.day.calc(data))

    def test_basement(self):
        datas = '())'
        self.assertEqual(3, self.day.floor(datas))
        datas = '()())))))))))'
        self.assertEqual(5, self.day.floor(datas))
