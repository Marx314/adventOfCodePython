from copy import deepcopy
from src import split_data


class Day18:
    def __init__(self):
        pass

    @split_data
    def calc_light_on(self, instructions, step=1):
        return sum([sum(l) for l in self._calc_light_matrix(instructions, step)])

    @split_data
    def calc_light_matrix(self, instructions, step=1):
        return self._calc_light_matrix(instructions, step)

    @split_data
    def calc_light_on_corner(self, instructions, step):
        light_map = self._convert_to_light_map(instructions)
        for i in xrange(step):
            light_map = self.apply_step(light_map)
            self.light_corner(light_map)
        return sum([sum(l) for l in light_map])

    def light_corner(self, light_map):
        light_map[0][0] = 1
        light_map[0][len(light_map) - 1] = 1
        light_map[len(light_map) - 1][0] = 1
        light_map[len(light_map) - 1][len(light_map) - 1] = 1

    def _calc_light_matrix(self, instructions, step=1):
        light_map = self._convert_to_light_map(instructions)
        for i in xrange(step):
            light_map = self.apply_step(light_map)
        return light_map

    def apply_step(self, light_map):
        c = deepcopy(light_map)
        for i, line in enumerate(light_map):
            for j, light in enumerate(line):
                if light == 0:
                    if self.three_on(i, j, light_map):
                        c[i][j] = 1
                else:
                    if not self.two_or_three_on(i, j, light_map):
                        c[i][j] = 0
        return c

    def _convert_to_light_map(self, instructions):
        list = []
        for line in instructions:
            l = []
            for letter in line:
                if letter == '.':
                    l.append(0)
                else:
                    l.append(1)
            list.append(l)
        return list

    def three_on(self, i, j, light_map):
        on = self.get_on(i, j, light_map)
        return on == 3

    def get_on(self, i, j, light_map):
        sum = 0
        sum += light_map[i - 1][j - 1] if self.have_top_left(i, j, light_map) else 0
        sum += light_map[i - 1][j + 1] if self.have_top_right(i, j, light_map) else 0
        sum += light_map[i - 1][j] if self.have_top(i, j, light_map) else 0
        sum += light_map[i][j - 1] if self.have_left(i, j, light_map) else 0
        sum += light_map[i][j + 1] if self.have_right(i, j, light_map) else 0
        sum += light_map[i + 1][j - 1] if self.have_bottom_left(i, j, light_map) else 0
        sum += light_map[i + 1][j + 1] if self.have_bottom_right(i, j, light_map) else 0
        sum += light_map[i + 1][j] if self.have_bottom(i, j, light_map) else 0

        return sum

    def two_or_three_on(self, i, j, list):
        on = self.get_on(i, j, list)
        return on in xrange(2, 4)

    def have_top_left(self, i, j, list):
        return i > 0 and j > 0

    def have_top_right(self, i, j, list):
        return i is not 0 and j < len(list) - 1

    def have_top(self, i, j, list):
        return i is not 0

    def have_left(self, i, j, list):
        return j > 0

    def have_right(self, i, j, list):
        return j < len(list) - 1

    def have_bottom_left(self, i, j, list):
        return i < len(list) - 1 and j > 0

    def have_bottom_right(self, i, j, list):
        return i < len(list) - 1 and j < len(list) - 1

    def have_bottom(self, i, j, list):
        return i < len(list) - 1
