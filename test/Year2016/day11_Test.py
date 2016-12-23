from unittest import TestCase
import unittest
from src.Year2016.Day11 import Day11


class Day11Test(TestCase):
    def setUp(self):
        self.day = Day11()

    def test_base(self):
        instructions = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''
        floor_plan = self.day.generate_initial(instructions)

        result = self.day.get_cost_of_shortest_path(floor_plan)
        self.assertEqual(result, 11)

    def test_puzzle(self):
        floor_plan = self.day.generate_initial(self.puzzle())

        result = self.day.get_cost_of_shortest_path(floor_plan)
        self.assertEqual(result, 31)

    @unittest.skip('wait a minute')
    def test_puzzle_part2(self):
        floor_plan = self.day.generate_initial(self.puzzle())
        floor_plan.floor_plan[0]['g'].append(-1)
        floor_plan.floor_plan[0]['g'].append(-2)
        floor_plan.floor_plan[0]['m'].append(1)
        floor_plan.floor_plan[0]['m'].append(2)

        result = self.day.get_cost_of_shortest_path(floor_plan)
        self.assertEqual(result, 55)

    def puzzle(self):
        return '''The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.'''
