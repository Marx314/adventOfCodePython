from math import floor
import re
from src import split_data


class Day14(object):
    def __init__(self):
        pass

    @split_data
    def max_distance(self, instructions, time):
        john = self._build_john(instructions, time)
        return max([deer['distance'] for deer in john])

    @split_data
    def max_point(self, instructions, time):
        john = self._build_john(instructions, time)
        for i in range(time + 1):
            for deer in john:
                if i % (deer['burst_time'] + deer['rest_time']) < deer['burst_time']:
                    deer['race'] += deer['speed']
            winner = max([deer['race'] for deer in john])
            for deer in john:
                if deer['race'] == winner:
                    deer['win'] += 1
        return max([deer['win'] for deer in john])

    def _build_john(self, instructions, time):
        return [self._handle_deer(re.split(r'\W+', instruction), time) for instruction in instructions]

    def _handle_deer(self, result, time):
        name = result[0]
        speed = int(result[3])
        burst_time = int(result[7])
        rest_time = int(result[14])
        distance = int(floor(time / (burst_time + rest_time)) * speed * burst_time + min(
            time - floor(time / (burst_time + rest_time)) * (burst_time + rest_time), burst_time) * speed)
        return {'name': name, 'speed': speed, 'burst_time': burst_time, 'rest_time': rest_time,
                'distance': distance, 'win': 0, 'race': 0}
