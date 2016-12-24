import itertools
import sys
import functools
from src.AStarSearch import AStarSearch, AStarSearchGraph


class A(AStarSearch):
    def heuristic(self, goal, current, next):
        return 1

    def search_until(self, current, goal):
        return current == goal


class Graph(AStarSearchGraph):
    def __init__(self, graph):
        self.graph = graph

    def neighbors(self, current):
        neighbors = [
            (current[0], current[1] + 1),
            (current[0], current[1] - 1),
            (current[0] + 1, current[1]),
            (current[0] - 1, current[1])
        ]
        return [n for n in neighbors if
                0 <= n[0] < len(self.graph) and 0 <= n[1] < len(self.graph[n[0]]) and self.graph[n[0]][n[1]] != '#']

    def cost(self, current, next):
        return 1


class Day24(object):
    graph = []
    length_caching = {}
    order_caching = {}

    def find_lowest_cost(self, puzzle):
        algorithm = A()
        self.graph = puzzle.split('\n')
        graph = Graph(self.graph)
        goals = puzzle.replace('.', '#').replace('\n', '#').replace('#', '').replace('0', '')

        orders = itertools.permutations(goals)
        lowest_cost = sys.maxsize
        for order in orders:
            cost = self._find_cost_for_order(algorithm, graph, order)
            if cost < lowest_cost:
                lowest_cost = cost
        return lowest_cost

    def find_lowest_cost_finishing_at_0(self, puzzle):
        algorithm = A()
        self.graph = puzzle.split('\n')
        graph = Graph(self.graph)
        goals = puzzle.replace('.', '#').replace('\n', '#').replace('#', '').replace('0', '')

        orders = itertools.permutations(goals)
        lowest_cost = sys.maxsize
        for order in orders:
            cost = self._find_cost_for_order(algorithm, graph, order)
            cost += self._shortest_path_between(algorithm, graph, self._find_(order[-1]), self._find_('0'))
            if cost < lowest_cost:
                lowest_cost = cost
        return lowest_cost

    def _find_cost_for_order(self, algorithm, graph, order):
        cost = 0
        starting = self._find_('0')
        for target in order:
            goal = self._find_(target)
            cost += self._shortest_path_between(algorithm, graph, starting, goal)
            starting = goal
        return cost

    def _shortest_path_between(self, algorithm, graph, origin, goal):
        if (origin, goal) not in self.length_caching:
            came_from, cost_so_far, current = algorithm.a_star_search(graph, origin, goal)
            self.length_caching[(origin, goal)] = cost_so_far[goal]
            self.length_caching[(goal, origin)] = cost_so_far[goal]
        return self.length_caching[(origin, goal)]

    def _find_(self, number):
        for x in range(len(self.graph)):
            for y in range(len(self.graph[x])):
                if self.graph[x][y] == number:
                    return x, y
