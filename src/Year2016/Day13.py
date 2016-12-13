import math
from queue import PriorityQueue

__author__ = 'maubry'
WALL = '#'
EMPTY = '_'


class Day13(object):
    def a_star_search(self, puzzle, destination, max_distance):
        # A* from http://www.redblobgames.com/pathfinding/a-star/implementation.html#python-astar
        frontier = PriorityQueue()
        position = (1, 1)
        current = (position, puzzle)
        frontier.put((0, current))
        came_from = {current: None}
        cost_so_far = {current: 0}
        heuristic = 0
        list_position = set()
        list_position.add((1, 1))
        while not frontier.empty():
            _, current = frontier.get()
            position, puzzle = current
            if position == destination:
                break

            moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            new_cost = cost_so_far[current] + 1
            for move in moves:
                new_position = (position[0] + move[0], position[1] + move[1])
                if new_position[0] < 0 or new_position[1] < 0:
                    continue
                if puzzle[new_position[1] * self.get_puzzle_size(puzzle) + new_position[0]] in (WALL, 'O'):
                    continue
                if cost_so_far[current] < max_distance:
                    list_position.add(new_position)

                new_puzzle = self.replace(puzzle, new_position)

                next = (new_position, new_puzzle)
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic
                    frontier.put((priority, next))
                    came_from[next] = current

        return cost_so_far, came_from, current, len(list_position)

    def build_puzzle(self, size, favorite_number=10):
        puzzle = ''.join([EMPTY for _ in range(size * size)])
        for i in range(size):
            for j in range(size):
                if self.is_wall(j, i, favorite_number):
                    puzzle = puzzle[:i * size + j] + WALL + puzzle[i * size + j + 1:]
        puzzle = self.replace(puzzle, (1, 1))

        return puzzle

    def is_wall(self, x, y, designer):
        binary_string = '{0:b}'.format(self.formula_designer(x, y, designer))
        ones = binary_string.count('1')
        return ones % 2 == 1

    def formula_designer(self, x, y, designer):
        return self.apply_formula(x, y) + designer

    @staticmethod
    def apply_formula(x, y):
        return x * x + 3 * x + 2 * x * y + y + y * y

    def replace(self, puzzle, move):
        size = self.get_puzzle_size(puzzle)
        return puzzle[:move[1] * size + move[0]] + 'O' + puzzle[move[1] * size + move[0] + 1:]

    @staticmethod
    def get_puzzle_size(puzzle):
        return int(math.sqrt(len(puzzle)))