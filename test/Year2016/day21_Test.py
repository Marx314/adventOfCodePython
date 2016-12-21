import unittest
from unittest import TestCase

from src.Year2016.Day21 import Day21


class Day21Test(TestCase):
    def setUp(self):
        self.day = Day21()

    def test_simple_instruction(self):
        password = 'abcde'
        instruction = 'swap position 4 with position 0'
        new_password = self.day.scramble_instruction(instruction, password)
        self.assertEqual(new_password, 'ebcda')
        instruction = 'swap letter d with letter b'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'edcba')
        instruction = 'reverse positions 0 through 4'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'abcde')
        instruction = 'rotate left 1 step'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'bcdea')
        instruction = 'move position 1 to position 4'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'bdeac')
        instruction = 'move position 3 to position 0'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'abdec')
        instruction = 'rotate based on position of letter b'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'ecabd')
        instruction = 'rotate based on position of letter d'
        new_password = self.day.scramble_instruction(instruction, new_password)
        self.assertEqual(new_password, 'decab')

    def test_apply_instructions(self):
        password = 'abcde'
        instructions = self.get_basic_instructions()
        scrambled = self.day.scramble(instructions, password=password)
        self.assertEqual(scrambled, 'decab')

    def test_puzzle(self):
        scrambled = self.day.scramble(self.puzzle(), password='abcdefgh')
        self.assertEqual(scrambled, 'ghfacdbe')

    def test_brute_force_simple(self):
        valid_password = self.day.brute_force_password(self.get_basic_instructions(), 'decab')
        self.assertIn('abcde', valid_password)

    @unittest.skip('roughly 40 seconds')
    def test_puzzle_part2(self):
        valid_password = self.day.brute_force_password(self.puzzle(), 'fbgdceah')
        self.assertIn('fhgcdaeb', valid_password)

    def get_basic_instructions(self):
        return '''swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d'''

    def puzzle(self):
        return '''rotate based on position of letter d
move position 1 to position 6
swap position 3 with position 6
rotate based on position of letter c
swap position 0 with position 1
rotate right 5 steps
rotate left 3 steps
rotate based on position of letter b
swap position 0 with position 2
rotate based on position of letter g
rotate left 0 steps
reverse positions 0 through 3
rotate based on position of letter a
rotate based on position of letter h
rotate based on position of letter a
rotate based on position of letter g
rotate left 5 steps
move position 3 to position 7
rotate right 5 steps
rotate based on position of letter f
rotate right 7 steps
rotate based on position of letter a
rotate right 6 steps
rotate based on position of letter a
swap letter c with letter f
reverse positions 2 through 6
rotate left 1 step
reverse positions 3 through 5
rotate based on position of letter f
swap position 6 with position 5
swap letter h with letter e
move position 1 to position 3
swap letter c with letter h
reverse positions 4 through 7
swap letter f with letter h
rotate based on position of letter f
rotate based on position of letter g
reverse positions 3 through 4
rotate left 7 steps
swap letter h with letter a
rotate based on position of letter e
rotate based on position of letter f
rotate based on position of letter g
move position 5 to position 0
rotate based on position of letter c
reverse positions 3 through 6
rotate right 4 steps
move position 1 to position 2
reverse positions 3 through 6
swap letter g with letter a
rotate based on position of letter d
rotate based on position of letter a
swap position 0 with position 7
rotate left 7 steps
rotate right 2 steps
rotate right 6 steps
rotate based on position of letter b
rotate right 2 steps
swap position 7 with position 4
rotate left 4 steps
rotate left 3 steps
swap position 2 with position 7
move position 5 to position 4
rotate right 3 steps
rotate based on position of letter g
move position 1 to position 2
swap position 7 with position 0
move position 4 to position 6
move position 3 to position 0
rotate based on position of letter f
swap letter g with letter d
swap position 1 with position 5
reverse positions 0 through 2
swap position 7 with position 3
rotate based on position of letter g
swap letter c with letter a
rotate based on position of letter g
reverse positions 3 through 5
move position 6 to position 3
swap letter b with letter e
reverse positions 5 through 6
move position 6 to position 7
swap letter a with letter e
swap position 6 with position 2
move position 4 to position 5
rotate left 5 steps
swap letter a with letter d
swap letter e with letter g
swap position 3 with position 7
reverse positions 0 through 5
swap position 5 with position 7
swap position 1 with position 7
swap position 1 with position 7
rotate right 7 steps
swap letter f with letter a
reverse positions 0 through 7
rotate based on position of letter d
reverse positions 2 through 4
swap position 7 with position 1
swap letter a with letter h'''
