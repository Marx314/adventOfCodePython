import operator
from collections import deque
from functools import reduce
from unittest import TestCase


def knot_hash_p1(lengths, size=5):
    lengths = [int(i.strip()) for i in lengths.split(',')]

    return knot_hash(lengths, size)


def knot_hash(lengths, stream_length=5):
    current_position = 0
    l = deque(list(range(stream_length)))
    for skip, i in enumerate(lengths):
        l.rotate(stream_length - current_position)
        p = list(l)
        pre = p[:i]
        post = p[i:]
        l = deque(pre[::-1] + post)
        l.rotate(-(stream_length - current_position))
        current_position = (current_position + i + skip) % stream_length

    return list(l)


def get_length(input):
    return list(map(ord, input))


def get_salted_length(input):
    return get_length(input) + [17, 31, 73, 47, 23]


def knot_hash_dense(length):
    sparse_hash = knot_hash(get_salted_length(length) * 64, 256)
    sparse_hashes = [sparse_hash[i:i + 16] for i in range(0, 256, 16)]
    dense = [sparse_to_dense(hash) for hash in sparse_hashes]

    return ''.join([format(d, '02x') for d in dense])


def sparse_to_dense(hash):
    return reduce(operator.xor, hash)


class Day10Test(TestCase):
    def test_simple_part1(self):
        self.assertEqual(knot_hash_p1('3'), [2, 1, 0, 3, 4])
        self.assertEqual(knot_hash_p1('3, 4'), [4, 3, 0, 1, 2])
        self.assertEqual(knot_hash_p1('3, 4, 1'), [4, 3, 0, 1, 2])
        self.assertEqual(knot_hash_p1('3, 4, 1, 5'), [3, 4, 2, 1, 0])

    def test_puzzle(self):
        i = knot_hash_p1(self.puzzle(), 256)
        self.assertEqual(i[0] * i[1], 8536)

    def sparse_xor(self):
        test_sparse_hash = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        self.assertEqual(sparse_to_dense(test_sparse_hash), 64)

    def test_part2(self):
        self.assertEqual(get_length('1,2,3'), [49, 44, 50, 44, 51])
        self.assertEqual(get_salted_length('1,2,3'), [49, 44, 50, 44, 51, 17, 31, 73, 47, 23])
        self.assertEqual(knot_hash_dense(''), 'a2582a3a0e66e6e86e3812dcb672a272')
        self.assertEqual(knot_hash_dense('AoC 2017'), '33efeb34ea91902bb2f59c9920caa6cd')
        self.assertEqual(knot_hash_dense('1,2,3'), '3efbe78a8d82f29979031a4aa0b16a9d')
        self.assertEqual(knot_hash_dense('1,2,4'), '63960835bcdc130f0b66d7ff4f6a5a8e')

    def test_puzzle_part2(self):
        self.assertEqual(knot_hash_dense(self.puzzle()), 'aff593797989d665349efe11bb4fd99b')

    def puzzle(self):
        return '''97,167,54,178,2,11,209,174,119,248,254,0,255,1,64,190'''
