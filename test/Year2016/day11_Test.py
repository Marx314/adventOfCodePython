from unittest import TestCase
import unittest

import re
from src import split_data
from src.Year2016.Day11 import Day11, FloorPlan


class Day11Test(TestCase):
    def setUp(self):
        self.day = Day11()

    def test_base(self):
        instructions = '''The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant.'''
        floor_plan = self.generate_initial(instructions)
        cost_so_far, came_from, current = self.day.a_star_search(floor_plan)
        self.assertEqual(cost_so_far[current], 11)

    def test_puzzle(self):
        floor_plan = self.generate_initial(self.puzzle())
        cost_so_far, came_from, current = self.day.a_star_search(floor_plan)
        states = self.build_state(came_from, cost_so_far, current)
        self.assertEqual(len(states), 31)

    @unittest.skip("Take about an hour to run with current heuristic")
    def test_puzzle_part2(self):
        floor_plan = self.generate_initial(self.puzzle())
        floor_plan.floor_plan[0]['g'].append(1)
        floor_plan.floor_plan[0]['g'].append(2)
        floor_plan.floor_plan[0]['m'].append(1)
        floor_plan.floor_plan[0]['m'].append(2)
        cost_so_far, came_from, current = self.day.a_star_search(floor_plan)
        states = self.build_state(came_from, cost_so_far, current)
        self.assertEqual(len(states), 55)

    def build_state(self, came_from, cost_so_far, current):
        index = cost_so_far[current]
        path = {index: came_from[current]}
        while index > 0:
            current = came_from[current]
            path[index] = current
            index -= 1

        return list(path.values())

    @split_data
    def generate_initial(self, instructions):
        floor_plan_list = [{'m': [], 'g': []} for _ in range(4)]
        element = {'hydrogen': 1, 'lithium': 2, 'thulium': 3, 'plutonium': 4, 'strontium': 5, 'promethium': 6,
                   'ruthenium': 7}
        for floor, instruction in enumerate(instructions):
            result = re.findall(r'((\w*\-?)*\s(microchip|generator))', instruction)
            for composant in result:
                if composant[2] == 'microchip':
                    floor_plan_list[floor]['m'].append(element[re.findall('\w*', composant[0])[0]])
                elif composant[2] == 'generator':
                    floor_plan_list[floor]['g'].append(element[re.findall('\w*', composant[0])[0]])

        return FloorPlan(floor_plan_list)

    def puzzle(self):
        return '''The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.'''
