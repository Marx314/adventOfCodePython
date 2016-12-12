import itertools
from queue import PriorityQueue
import copy


class Day11(object):
    def heuristic(self, new_floor_plan, current, cost_so_far):
        return (len(new_floor_plan._[3]['g']) + len(new_floor_plan._[3]['m'])) * -2

    def a_star_search(self, floor_plan):
        # A* from http://www.redblobgames.com/pathfinding/a-star/implementation.html#python-astar
        frontier = PriorityQueue()
        floor = 0
        current = (floor, floor_plan)
        frontier.put((0, current))
        came_from = {current: None}
        cost_so_far = {current: 0}
        directions = {0: [1], 1: [-1, 1], 2: [-1, 1], 3: [-1]}

        while not frontier.empty():
            _, current = frontier.get()
            floor, floor_plan = current
            if floor == 3 and repr(floor_plan).startswith('[][][][][][]'):
                break

            moves = self.generate_move(floor, floor_plan, 2) + self.generate_move(floor, floor_plan, 1)
            for move in moves:
                for direction in directions[floor]:
                    new_floor_plan = self.apply_move(floor, direction, floor_plan, move)
                    if not self.valid_floor(new_floor_plan.floor_plan[floor]):
                        continue
                    if not self.valid_floor(new_floor_plan.floor_plan[floor + direction]):
                        continue
                    new_cost = cost_so_far[current] + 1
                    next = (floor + direction, new_floor_plan)
                    if next not in cost_so_far or new_cost < cost_so_far[next]:
                        cost_so_far[next] = new_cost
                        priority = new_cost + self.heuristic(new_floor_plan, current, cost_so_far)
                        frontier.put((priority, next))
                        came_from[next] = current

        return cost_so_far, came_from, current

    @staticmethod
    def generate_move(floor, floor_plan, count=2):
        return list(itertools.combinations(floor_plan._[floor]['g'] + floor_plan._[floor]['m'], count))

    def apply_move(self, current_floor, direction, floor_plan, moves):
        new_floor_plan = FloorPlan(copy.deepcopy(floor_plan._))
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
        generators = sorted(floor['g'])
        microchips = sorted(floor['m'])
        no_generator = len(generators) == 0

        return generators == microchips or no_generator or all(m in generators for m in microchips)


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