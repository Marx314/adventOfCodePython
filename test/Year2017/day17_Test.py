from unittest import TestCase


def spinlock(step, size):
    result = [0]
    position = 0
    for i in range(1, size + 1):
        position = (position + step) % i + 1
        result.insert(position, i)

    return result, position


def angry_spinlock(step, size):
    result = [0]
    position = 0
    for i in range(1, size + 1):
        position = (position + step) % i + 1
        if position == 1:
            result.insert(position, i)
    return result


class Day17Test(TestCase):
    def test_simple_dance(self):
        self.assertEqual(spinlock(3, 1), ([0, 1], 1))
        self.assertEqual(spinlock(3, 2), ([0, 2, 1], 1))
        self.assertEqual(spinlock(3, 3), ([0, 2, 3, 1], 2))
        self.assertEqual(spinlock(3, 4), ([0, 2, 4, 3, 1], 2))
        self.assertEqual(spinlock(3, 6), ([0, 5, 2, 4, 3, 6, 1], 5))
        result, last_position = spinlock(3, 6)
        self.assertEqual(result[last_position + 1], 1)
        result, last_position = spinlock(3, 2017)
        self.assertEqual(result[last_position + 1], 638)

    def test_simple_part2(self):
        self.assertEqual(angry_spinlock(3, 1), [0, 1])
        self.assertEqual(angry_spinlock(3, 2), [0, 2, 1])
        self.assertEqual(angry_spinlock(3, 4), [0, 2, 1])

    def test_puzzle(self):
        result, last_position = spinlock(self.puzzle(), 2017)
        self.assertEqual(result[last_position + 1], 1670)

        result = angry_spinlock(self.puzzle(), 50000000)
        self.assertEqual(result[1], 2316253)

    def puzzle(self):
        return 328
