import itertools
import re
import copy
from src import split_data
from src.AStarSearch import AStarSearch


class Day11(AStarSearch):
    directions = {0: [1], 1: [-1, 1], 2: [-1, 1], 3: [-1]}

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
                    floor_plan_list[floor]['g'].append(-element[re.findall('\w*', composant[0])[0]])

        return FloorPlan(floor_plan_list)

    def get_cost_of_shortest_path(self, floor_plan):
        came_from, cost_so_far, current = self.a_star_search(self, (0, floor_plan), (3, '[][][][][][]'))
        return cost_so_far[current]

    def heuristic(self, current, next):
        floor_plan = next[1]
        return (len(floor_plan.floor_plan[3]['g']) + len(floor_plan.floor_plan[3]['m'])) * -10

    def cost(self, current, next):
        return 1

    def neighbors(self, current):
        floor, floor_plan = current
        moves = self.generate_move(floor, floor_plan, 2) + self.generate_move(floor, floor_plan, 1)
        neighbors = []
        for move in moves:
            for direction in self.directions[floor]:
                new_floor_plan = self.apply_move(floor, direction, floor_plan, move)
                if not self.valid_floor(new_floor_plan.floor_plan[floor]):
                    continue
                if not self.valid_floor(new_floor_plan.floor_plan[floor + direction]):
                    continue
                neighbors.append((floor + direction, new_floor_plan))
        return neighbors

    def search_until(self, current, goal):
        floor, floor_plan = current
        goal_floor, goal_floor_plan = goal
        return floor == goal_floor and repr(floor_plan).startswith(goal_floor_plan)

    @staticmethod
    def generate_move(floor, floor_plan, count=2):
        return list(
            itertools.combinations(floor_plan.floor_plan[floor]['g'] + floor_plan.floor_plan[floor]['m'], count))

    def apply_move(self, current_floor, direction, floor_plan, moves):
        new_floor_plan = FloorPlan(copy.deepcopy(floor_plan.floor_plan))
        for move in moves:
            if move in new_floor_plan.floor_plan[current_floor]['g']:
                self.move(move, new_floor_plan.floor_plan, current_floor, 'g', direction)
            elif move in new_floor_plan.floor_plan[current_floor]['m']:
                self.move(move, new_floor_plan.floor_plan, current_floor, 'm', direction)
        return new_floor_plan

    @staticmethod
    def move(item, floor_plan, floor, item_type, direction):
        if item in floor_plan[floor][item_type]:
            floor_plan[floor][item_type].remove(item)
        floor_plan[floor + direction][item_type].append(item)

    @staticmethod
    def valid_floor(floor):
        generators = sorted(map(lambda x: -x, floor['g']))
        microchips = sorted(floor['m'])
        no_generator = len(generators) == 0

        return generators == microchips or no_generator or all([m in generators for m in microchips])


class FloorPlan(object):
    def __init__(self, floor_plan):
        self.floor_plan = floor_plan

    def __hash__(self):
        return self.__repr__().__hash__()

    def __lt__(self, other):
        return repr(self) > repr(other)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __repr__(self):
        plan = ''
        for floor in self.floor_plan:
            plan += '{}'.format(sorted(floor['g']))
            plan += '{}'.format(sorted(floor['m']))
        return plan
