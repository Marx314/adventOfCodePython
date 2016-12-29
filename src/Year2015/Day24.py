from functools import reduce
import itertools
from operator import mul
from src import split_data


class Day24(object):
    @staticmethod
    def get_first_quantum_entanglement(weight_list, packages_count=3):
        mass = sum(weight_list)
        group_weight = int(mass / packages_count)
        group_weight_without_front = (packages_count - 1) * group_weight
        groups = set()
        group_size = 1
        while len(groups) == 0:
            for group in itertools.permutations(weight_list, r=group_size):
                if sum(group) == group_weight:
                    if sum([weight for weight in weight_list if weight not in group]) == group_weight_without_front:
                        groups.add(tuple(sorted(group)))
            group_size += 1
        groups = sorted(groups, key=len)
        qe = sorted([reduce(mul, group, 1) for group in groups])

        return qe[0]

    @split_data
    def make_list(self, instructions):
        return list(map(int, instructions))
