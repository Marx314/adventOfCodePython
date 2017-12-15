import unittest
from unittest import TestCase


def generator(n, factor):
    while True:
        n = (n * factor) % 2147483647
        yield n


def generator_picky(n, factor, modulo):
    while True:
        n = (n * factor) % 2147483647
        if n % modulo != 0:
            continue
        yield n


def generate_match(a, b, count):
    found = 0
    generator_a = generator(a, 16807)
    generator_b = generator(b, 48271)
    for _ in range(count):
        a = next(generator_a)
        b = next(generator_b)
        if bin(a)[-16:] == bin(b)[-16:]:
            found += 1
    return found


def generate_match_picky(a, b, count):
    found = 0
    ga = generator_picky(a, 16807, 4)
    gb = generator_picky(b, 48271, 8)
    for _ in range(count):
        a = next(ga)
        b = next(gb)
        if bin(a)[-16:] == bin(b)[-16:]:
            found += 1
    return found


class Day15Test(TestCase):
    def test_simple_generator(self):
        ga = generator(65, 16807)
        gb = generator(8921, 48271)
        self.assertEqual(next(ga), 1092455)
        self.assertEqual(next(ga), 1181022009)
        self.assertEqual(next(gb), 430625591)
        self.assertEqual(next(gb), 1233683848)
        self.assertEqual(generate_match(65, 8921, 3), 1)

    @unittest.skip("too long didn't wait")
    def test_simple_forty_millions(self):
        self.assertEqual(generate_match(65, 8921, 40000000), 588)

    def test_simple_picky_generator(self):
        ga = generator_picky(65, 16807, 4)
        gb = generator_picky(8921, 48271, 8)
        self.assertEqual(next(ga), 1352636452)
        self.assertEqual(next(ga), 1992081072)
        self.assertEqual(next(gb), 1233683848)
        self.assertEqual(next(gb), 862516352)
        self.assertEqual(generate_match_picky(65, 8921, 1055), 0)
        self.assertEqual(generate_match_picky(65, 8921, 1056), 1)

    @unittest.skip("wait a minute")
    def test_puzzle(self):
        self.assertEqual(generate_match(679, 771, 40000000), 626)
        self.assertEqual(generate_match_picky(679, 771, 5000000), 306)

    def puzzle(self):
        return '''Generator A starts with 679
Generator B starts with 771'''
