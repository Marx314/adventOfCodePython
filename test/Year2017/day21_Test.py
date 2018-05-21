import itertools
import math
from unittest import TestCase

import numpy

def blockshaped(arr, nrows, ncols):
    h, w = arr.shape
    return (arr.reshape(h // nrows, nrows, -1, ncols)
            .swapaxes(1, 2)
            .reshape(-1, nrows, ncols))


def apply_books(book, iteration):
    image = '''.#./..#/###'''.replace('/', '')
    rules = build_rules(book)

    for i in range(iteration):
        n = int(math.sqrt(len(image)))
        split = 2 if n % 2 == 0 else 3
        image = process(rules, image, split)

    n = int(math.sqrt(len(image)))
    return '/'.join([image[i:i + n] for i in range(0, len(image), n)])


def build_rules(book):
    rules = {}
    for rule in book.split('\n'):
        key, destination = map(lambda x: x.strip().replace('/', ''), rule.split('=>'))
        rules[key] = destination
        n = int(math.sqrt(len(key)))
        d = numpy.array([list(key[i:i + n]) for i in range(0, len(key), n)])
        add_to_rules(numpy.fliplr(d), destination, rules)
        add_to_rules(numpy.rot90(d, 1), destination, rules)
        add_to_rules(numpy.fliplr(numpy.rot90(d, 1)), destination, rules)
        add_to_rules(numpy.rot90(d, 2), destination, rules)
        add_to_rules(numpy.fliplr(numpy.rot90(d, 2)), destination, rules)
    return rules


def add_to_rules(numpy_array, destination, rules):
    rules[''.join(itertools.chain.from_iterable(numpy_array))] = destination


def process(rules, image, split):
    image_size = int(math.sqrt(len(image)))
    blocks = blockshaped(numpy.array([list(image[i:i + image_size]) for i in range(0, len(image), image_size)]), split, split)
    subimages = []
    for block_id in range(len(blocks)):
        subimage = ''.join(itertools.chain.from_iterable(blocks[block_id]))
        if len(subimage) in [4, 9]:
            subimage = rules[subimage]
        else:
            image_size = int(math.sqrt(len(image)))
            split = 2 if image_size % 2 == 0 else 3
            subimage = process(rules, subimage, split)
        subimages.append(subimage)

    z = int(math.sqrt(len(subimages[0])))

    lines = []
    line = []
    for subimage in subimages:
        if len(line) == int(image_size / split):
            lines.append(numpy.hstack(line))
            line = []
        line.append([list(subimage[i:i + z]) for i in range(0, len(subimage), z)])
    lines.append(numpy.hstack(line))

    return ''.join(itertools.chain.from_iterable(numpy.vstack(lines)))


class Day21Test(TestCase):
    def test_simple_test(self):
        book = '''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#'''
        self.assertEqual(apply_books(book, 1), '#..#/..../..../#..#')
        self.assertEqual(apply_books(book, 2), '##.##./#..#../....../##.##./#..#../......')
        self.assertEqual(apply_books(book, 2).count('#'), 12)

    def test_puzzle_part1(self):
        self.assertEqual(apply_books(self.puzzle(), 5).count('#'), 120)

    def test_puzzle_part2(self):
        self.assertEqual(apply_books(self.puzzle(), 18).count('#'), 2204099)

    def puzzle(self):
        return '''../.. => ..#/.#./...
#./.. => .../#../.##
##/.. => .##/###/##.
.#/#. => #.#/..#/#.#
##/#. => .../.##/...
##/## => ##./..#/..#
.../.../... => ##../..../##../.###
#../.../... => ...#/.#.#/.#../.#.#
.#./.../... => #.#./...#/#.#./.##.
##./.../... => ..#./#.##/#.../.###
#.#/.../... => ##../##.#/..#./#.##
###/.../... => ..../.#.#/.###/#..#
.#./#../... => #..#/#.../.##./....
##./#../... => #.##/..##/####/.###
..#/#../... => ..#./#.##/####/####
#.#/#../... => .##./#.##/#.#./##.#
.##/#../... => #.##/####/.###/...#
###/#../... => ..../#.#./##.#/..##
.../.#./... => .###/.##./##../.##.
#../.#./... => ..../#.##/...#/#.#.
.#./.#./... => ...#/####/.##./#...
##./.#./... => .###/#.##/###./....
#.#/.#./... => #.##/###./..../..#.
###/.#./... => .#../#.#./#.##/#.##
.#./##./... => .###/##../..##/#..#
##./##./... => ..#./#.#./.#.#/##.#
..#/##./... => .#../####/...#/..##
#.#/##./... => ..../##.#/.##./....
.##/##./... => .#.#/.#.#/.##./####
###/##./... => ##.#/..../..../....
.../#.#/... => ..##/##../##.#/###.
#../#.#/... => ####/#.##/#.../###.
.#./#.#/... => ..../#..#/..##/.#..
##./#.#/... => #.../..##/##../..#.
#.#/#.#/... => ...#/#.#./#.#./#...
###/#.#/... => ###./###./##.#/###.
.../###/... => ..#./###./##.#/####
#../###/... => ##.#/..#./##../..##
.#./###/... => #.../#.##/##../....
##./###/... => ..##/.#.#/#..#/#.##
#.#/###/... => #.##/..#./.#../..##
###/###/... => ..#./#..#/####/.##.
..#/.../#.. => ##.#/#.##/...#/###.
#.#/.../#.. => #..#/..#./##../###.
.##/.../#.. => ..#./.#../###./#.#.
###/.../#.. => ...#/...#/.#.#/.##.
.##/#../#.. => ##../#.#./#..#/##..
###/#../#.. => ##../.#.#/##../#..#
..#/.#./#.. => ##.#/##.#/...#/.#..
#.#/.#./#.. => .###/.#.#/###./....
.##/.#./#.. => #..#/###./####/..#.
###/.#./#.. => ..#./.###/.###/...#
.##/##./#.. => #.##/..##/...#/.###
###/##./#.. => ####/##.#/#.##/#..#
#../..#/#.. => ..../.##./#.##/#...
.#./..#/#.. => #..#/##../...#/#...
##./..#/#.. => ..#./.###/..##/.#.#
#.#/..#/#.. => .##./..##/..#./#..#
.##/..#/#.. => ####/.#.#/#.../.#.#
###/..#/#.. => ..../..##/#.##/###.
#../#.#/#.. => #.##/.#.#/.#../.##.
.#./#.#/#.. => ..##/###./.###/###.
##./#.#/#.. => ##.#/##.#/#.#./##..
..#/#.#/#.. => ###./###./.#.#/.#..
#.#/#.#/#.. => ##../..#./##../....
.##/#.#/#.. => .###/#.#./##.#/##..
###/#.#/#.. => ##.#/#.#./.#.#/#...
#../.##/#.. => .#.#/...#/.#.#/..#.
.#./.##/#.. => ###./##../##.#/....
##./.##/#.. => ..##/###./#.#./#.#.
#.#/.##/#.. => ##.#/..##/#..#/####
.##/.##/#.. => ..../####/..#./##..
###/.##/#.. => .###/#..#/..../.#..
#../###/#.. => #..#/.#../.#.#/#...
.#./###/#.. => .#../..../.##./.###
##./###/#.. => ##.#/.#../.#.#/#..#
..#/###/#.. => #.##/##../..##/#...
#.#/###/#.. => ####/..##/.#../##.#
.##/###/#.. => .###/#..#/.###/#.##
###/###/#.. => ..##/.##./##../#..#
.#./#.#/.#. => ..##/.##./.##./.###
##./#.#/.#. => ..##/...#/.##./####
#.#/#.#/.#. => .###/.###/#.#./.#..
###/#.#/.#. => ##.#/###./##.#/####
.#./###/.#. => ...#/..#./.#.#/.#..
##./###/.#. => ###./##.#/#.../#.#.
#.#/###/.#. => .##./#.#./...#/..#.
###/###/.#. => .#.#/.#../..##/####
#.#/..#/##. => .##./...#/#..#/.###
###/..#/##. => #.##/.#.#/...#/..##
.##/#.#/##. => ###./.###/...#/....
###/#.#/##. => .##./.##./#.#./#...
#.#/.##/##. => #.#./.##./.#.#/.###
###/.##/##. => ..../####/.#.#/#.##
.##/###/##. => .##./.###/###./.#..
###/###/##. => #.../###./.##./##.#
#.#/.../#.# => #.#./..../#.##/###.
###/.../#.# => .#../.#.#/#.../.###
###/#../#.# => ###./#..#/####/##..
#.#/.#./#.# => ###./##.#/..../.#..
###/.#./#.# => ####/.#.#/.#../..##
###/##./#.# => #.#./####/..##/#...
#.#/#.#/#.# => #.#./#.#./#.../#.##
###/#.#/#.# => #.##/.#../..#./.##.
#.#/###/#.# => .###/..##/####/#..#
###/###/#.# => #.../..#./..#./#.##
###/#.#/### => .#.#/.###/#.##/..##
###/###/### => #.#./...#/.#../.#.#'''