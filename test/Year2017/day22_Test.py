import unittest
from enum import Enum
from unittest import TestCase


class Status(Enum):
    CLEAN = 0
    WEAK = 1
    INFECTED = 2
    FLAGGED = 3


directions = {
    'up': (0, -1),
    'left': (-1, 0),
    'down': (0, 1),
    'right': (1, 0)
}
turn_right = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
turn_left = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}
flip = {'up': 'down', 'left': 'right', 'down': 'up', 'right': 'left'}


def generate_infected2(cluster, bursts):
    split_cluster = cluster.split('\n')
    infected = get_infected(split_cluster)

    position = (int(len(split_cluster[0]) / 2), int(len(split_cluster) / 2))
    direction = 'up'
    useful_burst = 0

    for _ in range(bursts):
        if position in infected:
            if infected[position] is Status.INFECTED:
                direction = turn_right[direction]
                infected[position] = Status.FLAGGED
            elif infected[position] is Status.WEAK:
                useful_burst += 1
                infected[position] = Status.INFECTED
            elif infected[position] is Status.FLAGGED:
                direction = flip[direction]
                del infected[position]
        else:
            direction = turn_left[direction]
            infected[position] = Status.WEAK
        position = position[0] + directions[direction][0], position[1] + directions[direction][1]

    return useful_burst


def generate_infected(cluster, bursts):
    split_cluster = cluster.split('\n')
    infected = get_infected(split_cluster)

    position = (int(len(split_cluster[0]) / 2), int(len(split_cluster) / 2))
    direction = 'up'
    useful_burst = 0

    for _ in range(bursts):
        if position in infected and infected[position] is Status.INFECTED:
            direction = turn_right[direction]
            infected[position] = Status.CLEAN
            del infected[position]
        else:
            useful_burst += 1
            direction = turn_left[direction]
            infected[position] = Status.INFECTED
        position = position[0] + directions[direction][0], position[1] + directions[direction][1]

    return useful_burst


def get_infected(cluster):
    infected = {}
    for y, line in enumerate(cluster):
        for x, node in enumerate(line):
            if node == '#':
                infected[(x, y)] = Status.INFECTED
    return infected


def print_puzzle(current_position, infected):
    min_y = min([i[0] for i in infected])
    max_y = max([i[0] for i in infected])
    min_x = min([i[1] for i in infected])
    max_x = max([i[1] for i in infected])
    for y in range(min_y, max_y):
        line = []
        for x in range(min_x, max_x):
            if (x, y) in infected:
                if current_position == (x, y):
                    line.append('Q')
                else:
                    line.append('#')
            else:
                if current_position == (x, y):
                    line.append('_')
                else:
                    line.append('.')
        print(''.join(line))


class Day22Test(TestCase):
    def simple_puzzle(self):
        return '''..#
#..
...'''

    def test_simple_test(self):
        self.assertEqual(generate_infected(self.simple_puzzle(), 0), 0)
        self.assertEqual(generate_infected(self.simple_puzzle(), 1), 1)
        self.assertEqual(generate_infected(self.simple_puzzle(), 2), 1)
        self.assertEqual(generate_infected(self.simple_puzzle(), 3), 2)
        self.assertEqual(generate_infected(self.simple_puzzle(), 6), 5)
        self.assertEqual(generate_infected(self.simple_puzzle(), 7), 5)
        self.assertEqual(generate_infected(self.simple_puzzle(), 70), 41)
        self.assertEqual(generate_infected(self.simple_puzzle(), 10000), 5587)

    def test_puzzle(self):
        self.assertEqual(generate_infected(self.puzzle(), 10000), 5266)

    def test_simple_part2(self):
        self.assertEqual(generate_infected2(self.simple_puzzle(), 100), 26)

    @unittest.skip('too long')
    def test_simple_part2_over9000(self):
        self.assertEqual(generate_infected2(self.simple_puzzle(), 10000000), 2511944)

    @unittest.skip('too long')
    def test_puzzle2(self):
        self.assertEqual(generate_infected2(self.puzzle(), 10000000), 2511895)

    def puzzle(self):
        return '''.########.....#...##.####
....#..#.#.##.###..#.##..
##.#.#..#.###.####.##.#..
####...#...####...#.##.##
..#...###.#####.....##.##
..#.##.######.#...###...#
.#....###..##....##...##.
##.##..####.#.######...##
#...#..##.....#..#...#..#
........#.##..###.#.....#
#.#..######.#.###..#...#.
.#.##.##..##.####.....##.
.....##..#....#####.#.#..
...#.#.#..####.#..###..#.
##.#..##..##....#####.#..
.#.#..##...#.#####....##.
.####.#.###.####...#####.
...#...######..#.##...#.#
#..######...#.####.#..#.#
...##..##.#.##.#.#.#....#
###..###.#..#.....#.##.##
..#....##...#..#..##..#..
.#.###.##.....#.###.#.###
####.##...#.#....#..##...
#.....#.#..#.##.#..###..#'''
