import itertools
from src import split_data


class Day17(object):
    def __init__(self):
        self.attributes = {}

    def labeled_container(self, i):
        def _():
            return i

        return _

    @split_data
    def generate_combinaison(self, instructions, liter=25):
        container_list = sorted([int(c) for c in instructions])
        m = [self.labeled_container(i) for i in container_list]
        min_size = self._get_min(container_list, liter)
        max_size = self._get_max(container_list, liter)
        all_valid_combinaison = []
        for size in range(min_size, max_size + 1):
            all_valid_combinaison += self._generate_for_size(liter, m, size)
        return self._get_combinaison_from_closure(all_valid_combinaison)

    @split_data
    def how_many_minimum(self, instructions, liter=25):
        container_list = sorted([int(c) for c in instructions])
        m = [self.labeled_container(i) for i in container_list]
        min_size = self._get_min(container_list, liter)
        return len(self._generate_for_size(liter, m, min_size))

    def _generate_for_size(self, liter, m, size):
        return [combinaison for combinaison in list(itertools.combinations(m, size)) if
                self.is_valid_combinaison(combinaison, liter)]

    def _get_max(self, container_list, liter):
        for max_size in range(len(container_list), 1, -1):
            if liter <= sum(container_list[:max_size]):
                break
        return max_size

    def _get_min(self, container_list, liter):
        for min_size in range(1, len(container_list)):
            if liter <= sum(container_list[-min_size:]):
                break
        return min_size

    def is_valid_combinaison(self, combinaison, liter):
        return sum([container() for container in combinaison]) == liter

    def _get_combinaison_from_closure(self, all_valid_combinaison):
        return [[container() for container in combinaison] for combinaison in all_valid_combinaison]
