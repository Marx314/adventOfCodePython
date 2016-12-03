from itertools import permutations
from src import split_data


class Day9(object):
    def __init__(self):
        pass

    @split_data
    def calc(self, instructions, method=min):
        graph = {}
        cities = set()
        for instruction in instructions:
            result = instruction.split(' ')
            cities.add(result[0])
            cities.add(result[2])
            graph[(result[0], result[2])] = int(result[4])
            graph[(result[2], result[0])] = int(result[4])

        paths = self.generate_path(cities)
        cost_effective_path = dict()
        for path in paths:
            cost_effective_path[self.calculate(list(path), graph)] = path
        return method(cost_effective_path.keys())

    def generate_path(self, cities):
        return [perm for i, perm in enumerate(permutations(cities))]

    def calculate(self, path, graph):
        return sum([graph[(path[i], path[i + 1])] for i in range(len(path) - 1)])
