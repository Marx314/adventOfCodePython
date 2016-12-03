WEST = 'west'
SOUTH = 'south'
EAST = 'east'
NORTH = 'north'


class Day1(object):
    def calc(self, datas):
        direction, directions, moves, result = self._initialize(datas)
        for move in moves:
            direction = Day1._get_direction(direction, move)
            result[directions[direction]] += int(move[1:])

        distance = abs(result[NORTH] - result[SOUTH]) + abs(result[EAST] - result[WEST])
        result['distance'] = distance
        return result

    def distance_from_first_crossing_path(self, datas):
        direction, directions, moves, result = self._initialize(datas)
        positions = [(0, 0)]
        for move in moves:
            direction = Day1._get_direction(direction, move)
            for i in range(int(move[1:])):
                result[directions[direction]] += 1
                new_position = (result[NORTH] - result[SOUTH], result[EAST] - result[WEST])
                if new_position in positions:
                    return abs(new_position[0]) + abs(new_position[1])
                positions.append(new_position)

    @staticmethod
    def _get_direction(direction, move):
        if move[0] == 'L':
            direction -= 1
        elif move[0] == 'R':
            direction += 1
        if direction == -1:
            direction = 3
        if direction == 4:
            direction = 0
        return direction

    @staticmethod
    def _initialize(datas):
        moves = datas.split(', ')
        directions = [NORTH, EAST, SOUTH, WEST]
        result = Day1._build_result(directions)
        direction = 0
        return direction, directions, moves, result

    @staticmethod
    def _build_result(directions):
        result = {}
        for direction in directions:
            result[direction] = 0
        return result
