import itertools
import functools
from src.AStarSearch import AStarSearch
from src.AStarSearch import AStarSearchGraph


class A(AStarSearch):
    def heuristic(self, goal, current, next):
        return 1

    def search_until(self, current, goal):
        return current == goal


class Graph(AStarSearchGraph):
    def __init__(self, graph):
        self.graph = graph.split('\n')
        self.width = len(self.graph)
        self.height = len(self.graph[0])

    def neighbors(self, current):
        neighbors = [
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1])
        ]
        return [n for n in neighbors if
                0 <= n[0] < self.width and 0 <= n[1] < self.height and self.graph[n[0]][n[1]] != '#']

    def cost(self, current, next):
        return 1


class Day24(object):
    graph = []

    def find_lowest_cost(self, puzzle, final_destination=None):
        self.graph = puzzle.split('\n')
        graph = Graph(puzzle)
        goals = puzzle.replace('.', '#').replace('\n', '#').replace('#', '').replace('0', '')

        orders = itertools.permutations(goals)
        costs = []
        for order in orders:
            if final_destination is not None:
                order += (final_destination,)
            costs.append(self._find_cost_for_order(graph, order))
        costs = sorted(costs)
        return costs[0]

    def _find_cost_for_order(self, graph, order):
        cost = 0
        starting = self._find_('0')
        for target_letter in order:
            goal = self._find_(target_letter)
            cost += self._shortest_path_between(graph, starting, goal)
            starting = goal
        return cost

    @staticmethod
    @functools.lru_cache()
    def _shortest_path_between(graph, origin, goal):
        came_from, cost_so_far, current = A().a_star_search(graph, origin, goal)
        return cost_so_far[goal]

    @functools.lru_cache()
    def _find_(self, number):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                if self.graph[x][y] == number:
                    return x, y
