from src import split_data


class Day3(object):
    @staticmethod
    def is_valid_triangle(input):
        side = sorted(input)
        return side[0] + side[1] > side[2]

    @split_data
    def count_valid_triangle_flip_data(self, lines):
        lines = [[int(i) for i in line.split(' ') if i != ''] for line in lines]
        possibilities = []
        for i in range(int(len(lines) / 3)):
            possibilities.append([lines[i * 3][0], lines[i * 3 + 1][0], lines[i * 3 + 2][0]])
            possibilities.append([lines[i * 3][1], lines[i * 3 + 1][1], lines[i * 3 + 2][1]])
            possibilities.append([lines[i * 3][2], lines[i * 3 + 1][2], lines[i * 3 + 2][2]])
        return self._how_many_valid(possibilities)

    def _how_many_valid(self, possibilities):
        valid = []
        for triangle in possibilities:
            if self.is_valid_triangle(triangle):
                valid.append(triangle)
        return len(valid)

    @split_data
    def count_valid_triangle(self, triangles):
        possibilities = []
        for triangle in triangles:
            possibilities.append([int(i) for i in triangle.split(' ') if i != ''])
        return self._how_many_valid(possibilities)
