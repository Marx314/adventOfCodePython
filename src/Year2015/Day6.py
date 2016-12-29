import re
from src import split_data


def _build_light_maps():
    return [[0 for _ in range(1000)] for _ in range(1000)]


def _how_many_on(light_map):
    return sum([sum(line) for line in light_map])


def _transform_data(instruction):
    pattern = r'([a-z\s]+)(\d+)\,(\d+)'
    result = re.split(pattern, instruction)
    return result[1], (int(result[6]), int(result[7])), (int(result[2]), int(result[3]))


class Day6(object):
    def __init__(self):
        pass

    @split_data
    def calc(self, instructions):
        lights_map = _build_light_maps()
        for instruction in instructions:
            do, end, start = _transform_data(instruction)
            for i in range(start[0], end[0] + 1):
                for j in range(start[1], end[1] + 1):
                    if do == 'turn on ':
                        lights_map[i][j] = 1
                    elif do == 'toggle ':
                        lights_map[i][j] = 1 if lights_map[i][j] == 0 else 0
                    elif do == 'turn off ':
                        lights_map[i][j] = 0

        return _how_many_on(lights_map)

    @split_data
    def calc_bright(self, instructions):
        lights_map = _build_light_maps()
        for instruction in instructions:
            do, end, start = _transform_data(instruction)
            for i in range(start[0], end[0] + 1):
                for j in range(start[1], end[1] + 1):
                    if do == 'turn on ':
                        lights_map[i][j] += 1
                    elif do == 'toggle ':
                        lights_map[i][j] += 2
                    elif do == 'turn off ':
                        lights_map[i][j] = lights_map[i][j] - 1 if lights_map[i][j] > 1 else 0

        return _how_many_on(lights_map)
