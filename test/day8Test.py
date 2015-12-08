from unittest import TestCase
from src.Day8 import Day8


class Day8Test(TestCase):
    def setUp(self):
        self.day = Day8()

    def tearDown(self):
        pass

    def test_empty_string(self):
        instructions = [r'""']
        self.assertEqual(2-0, self.day.calc(instructions))

    def test_abc(self):
        instructions = [r'"abc"']
        self.assertEqual(5-3, self.day.calc(instructions))

    def test_aaa_double_quote_aaa(self):
        instructions = [r'"aaa\"aaa"']
        self.assertEqual(10-7, self.day.calc(instructions))

    def test_hax0r_5(self):
        instructions = [r'"\x27a"']
        self.assertEqual(6-1, self.day.calc(instructions))

    def test_double_hax0r_8(self):
        instructions = [r'"\x27a\x27"']
        self.assertEqual(10-2, self.day.calc(instructions))

    def test_empty_string_encoded_6_2(self):
        instructions = [r'""']
        self.assertEqual(6-2, self.day.encoded(instructions))

    def test_encoded_abc_9_5(self):
        instructions = [r'"abc"']
        self.assertEqual(9-5, self.day.encoded(instructions))

    def test_encoded_aaa_double_quote_aaa_16_10(self):
        instructions = [r'"aaa\"aaa"']
        self.assertEqual(16-10, self.day.encoded(instructions))

    def test_encoded_hax0r_11_6(self):
        instructions = [r'"\x27"']
        self.assertEqual(11-6, self.day.encoded(instructions))

    def test_encoded_double_hax0r_16_10(self):
        instructions = [r'"\x27\x27"']
        self.assertEqual(16-10, self.day.encoded(instructions))

    def test_multiple_encoded_42_23(self):
        instructions = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
        self.assertEqual(42-23, self.day.encoded(instructions))
