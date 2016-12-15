import re
from src import split_data


class Day15(object):
    @staticmethod
    def position_in_time_function(initial, positions):
        return lambda x: (x + initial) % positions

    @split_data
    def get_perfect_timing(self, instructions):
        disc_positions_time_initial = r'(\d+)'
        slots = {}
        for instruction in instructions:
            disc, positions, time, initial = map(int, re.findall(disc_positions_time_initial, instruction))
            slots[disc] = Day15.position_in_time_function(initial, positions)
        index = 0
        expected = [0 for _ in range(len(instructions))]
        while True:
            timing = [slots[disc](i + index) for i, disc in enumerate(slots.keys())]
            if sorted(timing) == expected:
                return index - 1
            index += 1
