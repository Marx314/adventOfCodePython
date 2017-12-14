from unittest import TestCase

from src import split_data
from test.Year2017.day10_Test import knot_hash_dense


def get_line(key, line):
    row = get_bin_from_hash(knot_hash_dense('{}-{}'.format(key, line)))
    row = row.replace('0', '.')
    row = row.replace('1', '#')
    return row


def generate_partition(key, total_line):
    return '\n'.join([get_line(key, i) for i in range(total_line)])


def get_bin_from_hash(hash):
    return bin(int(hash, 16))[2:].rjust(128, '0')


@split_data
def region_count(partition):
    all = []
    for x, line in enumerate(partition):
        for y, square in enumerate(line):
            if square is '#':
                all.append((x, y))
    region = 0
    while all:
        queue = [all[0]]
        while queue:
            x, y = queue.pop()
            if (x, y) in all:
                all.remove((x, y))
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))
        region += 1
    return region


class Day14Test(TestCase):
    def test_simple_program_list(self):
        sample = '''flqrgnkx'''

        self.assertIn('1010000011000010000000010111', get_bin_from_hash('a0c2017'))
        self.assertEqual(get_line(sample, 0)[:8], '##.#.#..')
        partition = generate_partition(sample, 128)
        self.assertEqual(partition[:8], '##.#.#..')
        self.assertEqual(partition[129:129 + 8], '.#.#.#.#')
        self.assertEqual(partition[258:258 + 8], '....#.#.')
        self.assertEqual(partition[387:387 + 8], '#.#.##.#')
        self.assertEqual(partition.count('#'), 8108)

        self.assertEqual(region_count(partition), 1242)

    def test_puzzle(self):
        partition = generate_partition(self.puzzle(), 128)

        self.assertEqual(partition.count('#'), 8106)
        self.assertEqual(region_count(partition), 1242)

    def puzzle(self):
        return '''oundnydw'''
