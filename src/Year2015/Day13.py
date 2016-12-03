from itertools import permutations
import re
from src import split_data


class Day13(object):
    def __init__(self):
        self.ignore = None

    @split_data
    def seating(self, instructions, me=False):
        happiness = {}
        self._get_happiness_with_peoples(happiness, instructions)
        if me:
            self._add_me(happiness)

        seatings = self._generate_path(set([i[0] for i in happiness.keys()]))
        seating_by_happiness = dict()
        for seat in seatings:
            seating_by_happiness[self._happiness_level(list(seat), happiness)] = seat
        return max(seating_by_happiness.keys())

    def _get_happiness_with_peoples(self, happiness, instructions):
        [self.handle_result(happiness, re.split(r'\W+', instruction)) for instruction in instructions]

    def handle_result(self, happiness, result):
        happiness[(result[0], result[10])] = int(result[3]) * -1 if result[2] == 'lose' else int(result[3])

    def _generate_path(self, cities):
        return [perm for i, perm in enumerate(permutations(cities))]

    def _happiness_level(self, seat, happiness):
        left = sum([happiness[(seat[i], seat[i + 1])] for i in range(len(seat) - 1)])
        right = sum([happiness[(seat[i], seat[i - 1])] for i in range(len(seat) - 1, 0, -1)])
        left += happiness[(seat[0], seat[len(seat) - 1])]
        right += happiness[(seat[len(seat) - 1], seat[0])]

        return left + right

    def _add_me(self, happiness):
        yourself = "yourself"
        for people in set([i[0] for i in happiness.keys()]):
            happiness[(people, yourself)] = 0
            happiness[(yourself, people)] = 0
