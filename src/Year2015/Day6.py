import re
from src import split_data


class Day6(object):
    def __init__(self):
        pass

    @split_data
    def calc(self, instructions):
        lights_map = self._build_light_maps()
        for instruction in instructions:
            result = self._transform_data(instruction)
            do, end, start = self._get_instruction_start_end(result)
            self._apply(do, start, end, lights_map)

        return self._how_many_on(lights_map)

    @split_data
    def calc_bright(self, instructions):
        lights_map = self._build_light_maps()
        for instruction in instructions:
            result = self._transform_data(instruction)
            do, end, start = self._get_instruction_start_end(result)
            self._apply_bright(do, start, end, lights_map)

        return self._how_many_on(lights_map)

    def _build_light_maps(self):
        n = 1000
        lights_map = [[0 for x in range(n)] for y in range(n)]
        return lights_map

    def _how_many_on(self, light_map):
        calc = sum([sum(line) for line in light_map])
        return calc

    def _apply_bright(self, do, start, end, light_map):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if do == 'turn on ':
                    light_map[i][j] += 1
                elif do == 'toggle ':
                    light_map[i][j] += 2
                elif do == 'turn off ':
                    light_map[i][j] = light_map[i][j] - 1 if light_map[i][j] > 1 else 0

    def _apply(self, do, start, end, light_map):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if do == 'turn on ':
                    light_map[i][j] = 1
                elif do == 'toggle ':
                    light_map[i][j] = 1 if light_map[i][j] == 0 else 0
                elif do == 'turn off ':
                    light_map[i][j] = 0

    def _get_instruction_start_end(self, result):
        do = result[1]
        start = (int(result[2]), int(result[3]))
        end = (int(result[6]), int(result[7]))
        return do, end, start

    def _transform_data(self, instruction):
        pattern = r'([a-z\s]+)(\d+)\,(\d+)'
        result = re.split(pattern, instruction)
        return result