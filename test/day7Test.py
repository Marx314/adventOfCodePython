from unittest import TestCase
from src.Day7 import Day7


class Day7Test(TestCase):
    def setUp(self):
        self.day = Day7()

    def tearDown(self):
        pass

    def test_basic_simple_thread(self):
        instructions = [u'123 -> x']
        self.assertEqual({'x': 123}, self.day._apply_operations(instructions))
        instructions = [u'456 -> y']
        self.assertEqual({'y': 456}, self.day._apply_operations(instructions))
        instructions = [u'123 -> x', u'456 -> y', u'x AND y -> z']
        self.assertEqual({'x': 123, 'y': 456, 'z': 123 & 456}, self.day._apply_operations(instructions))

    def test_a_simple_set(self):
        instructions = [u'123 -> x', u'456 -> y', u'x AND y -> d', u'x OR y -> e', u'x LSHIFT 2 -> f', u'y RSHIFT 2 -> g', u'NOT x -> h', u'NOT y -> i']
        self.assertEqual({'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456},
                         self.day._apply_operations(instructions))

    def test_sort_simple_set(self):
        instructions = [u'x AND y -> d', u'x OR y -> e', u'x LSHIFT 2 -> f', u'y RSHIFT 2 -> g', u'NOT x -> h', u'NOT y -> i', u'123 -> x', u'456 -> y']
        self.assertEqual({'d': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079, 'x': 123, 'y': 456},
                         self.day._apply_operations(instructions))

    def test_sort_complex_set(self):
        instructions = [u'i -> j', u'y RSHIFT 2 -> g', u'NOT y -> i', u'123 -> x', u'456 -> y']
        self.assertEqual({'g': 114, 'i': 65079, 'j': 65079, 'x': 123, 'y': 456},
                         self.day._apply_operations(instructions))
