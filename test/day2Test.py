from unittest import TestCase
from src.Day2 import Day2


class Day2Test(TestCase):
    def setUp(self):
        self.day = Day2()

    def tearDown(self):
        pass

    def test_2x3x4(self):
        data = self.buildData("2x3x4")
        self.assertEqual(58, self.day.calc(data))

    def test_1x1x10(self):
        data = self.buildData("1x1x10")
        self.assertEqual(43, self.day.calc(data))

    def test_ribbon(self):
        data = self.buildData("2x3x4")
        self.assertEqual(34, self.day.ribbon(data))

    def test_ribbonTwo(self):
        data = self.buildData("1x1x10")
        self.assertEqual(14, self.day.ribbon(data))

    def test_ribbonCube(self):
        data = self.buildData("2x2x2")
        self.assertEqual(8+8, self.day.ribbon(data))

    def buildData(self, data):
        return "{0}\n".format(data)


