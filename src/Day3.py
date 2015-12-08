from src.InputFetcher import InputFetcher


class Day3:
    def __init__(self):
        pass

    def calc(self, data):
        position = [0, 0]
        santa_map = {0: {0: 1}}
        for direction in data:
            self._move_santa(direction, santa_map, position)

        count = 0
        for house_x in santa_map.keys():
            for house_y in santa_map[house_x].keys():
                count += 1
        return count

    def two_santa(self, data):
        santa_turn = True
        santa_position = [0, 0]
        robo_santa_position = [0, 0]
        santa_map = {0: {0: 1}}
        for direction in data:
            if santa_turn:
                position = santa_position
            else:
                position = robo_santa_position
            self._move_santa(direction, santa_map, position)
            santa_turn = not santa_turn

        count = 0
        for house_x in santa_map.keys():
            for house_y in santa_map[house_x].keys():
                count += 1
        return count

    def _create_position_if_needed(self, santa_map, position):
        if position[0] not in santa_map.keys():
            santa_map[position[0]] = {position[1]: 0}
        if position[1] not in santa_map[position[0]].keys():
            santa_map[position[0]][position[1]] = 0

    def _move_santa(self, direction, santa_map, position):
        if direction == '>':
            position[1] += 1
        if direction == '<':
            position[1] -= 1
        if direction == '^':
            position[0] += 1
        if direction == 'v':
            position[0] -= 1
        self._create_position_if_needed(santa_map, position)
        santa_map[position[0]][position[1]] += 1

    @staticmethod
    def run():
        data = InputFetcher.fetch_input(3)
        day = Day3()
        print data
        print day.calc(data)
        print day.two_santa(data)
Day3.run()
