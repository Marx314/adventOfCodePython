import math
from queue import PriorityQueue
from src.AStarSearch import AStarSearch

MOVES = [[0, 1], [0, -1], [1, 0], [-1, 0]]

WALL = '#'
EMPTY = '_'
PATH = 'O'


class Day13(AStarSearch):
    puzzle_size = 0

    def shortest_path_cost(self, puzzle, goal):
        self.puzzle_size = self.get_puzzle_size(puzzle)
        came_from, cost_so_far, current = self.a_star_search(self, ((1, 1), puzzle), (goal, ''))
        valid_end = sorted([cost for k, cost in cost_so_far.items() if k[0] == goal])
        return valid_end[0]

    def path_length_and_location_within_50_step(self, puzzle, goal):
        self.puzzle_size = self.get_puzzle_size(puzzle)
        came_from, cost_so_far, current = self.a_star_search(self, ((1, 1), puzzle), (goal, ''))

        path_length = sorted(set([cost for k, cost in cost_so_far.items() if k[0] == goal]))
        position_with_50_distance = set([k[0] for k, cost in cost_so_far.items() if cost <= 50])

        return path_length[0], len(position_with_50_distance)

    def heuristic(self, current, next):
        return 0

    def cost(self, current, next):
        return 1

    def search_until(self, current, goal):
        position, _ = current
        goal_position, _ = goal
        return position == goal_position

    def neighbors(self, current):
        position, puzzle = current
        neighbors = []
        for move in MOVES:
            new_position = (position[0] + move[0], position[1] + move[1])
            if new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= self.puzzle_size or new_position[
                1] >= self.puzzle_size:
                continue
            if puzzle[new_position[1] * self.puzzle_size + new_position[0]] in (WALL, PATH):
                continue
            new_puzzle = self.replace(puzzle, new_position)

            neighbors.append((new_position, new_puzzle))

        return neighbors

    def build_puzzle(self, size, favorite_number):
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
        return puzzle[:move[1] * size + move[0]] + PATH + puzzle[move[1] * size + move[0] + 1:]

    @staticmethod
    def get_puzzle_size(puzzle):
        return int(math.sqrt(len(puzzle)))
