import math
import sys
from unittest import TestCase


class Day3:
    def calculate_distance(self, goal):
        if goal == 1:
            return 0
        x = y = dx = 0
        dy = -1
        step = 0
        while step < goal - 1:
            step += 1
            if self.corner_case(x, y):
                dx, dy = -dy, dx
            x, y = x + dx, y + dy

        return abs(x) + abs(y)

    def corner_case(self, x, y):
        corner_bottom_left = (x < 0 and x == -y)
        corner_up_right = (x > 0 and x == 1 - y)
        corner_up_left_or_bottom_right = x == y

        return any([corner_up_left_or_bottom_right, corner_bottom_left, corner_up_right])

    # http://oeis.org/A141481 PARI to python
    # http://www.wolframalpha.com/input/?i=1,+1,+2,+4,+5,+10,+11,+23,+25,+26,+54,+57,+59,+122,+133,+142,+147,+304,+330,+351,+362,+...
    def A141481(self):
        center = sys.maxsize
        h = 2 * center - 1
        A = {(center, center): 1}
        T = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

        for n in range(1, (h - 2) * (h - 2) - 1):
            g = int(math.sqrt(n))
            r = divmod(g + g % 2, 2)[0]
            q = int(4 * r * r)
            d = n - q
            if n <= q - 2 * r:
                j = d + 3 * r
                k = r
            else:
                if n <= q:
                    j = r
                    k = -d - r
                else:
                    if n <= q + 2 * r:
                        j = r - d
                        k = -r
                    else:
                        j = -r
                        k = d - 3 * r
            j = int(j + center)
            k = int(k + center)
            s = 0
            for position in T:
                v = [j, k]
                v[0] += position[0]
                v[1] += position[1]
                if (v[0], v[1]) in A:
                    s += A[(v[0], v[1])]
            A[(j, k)] = s
            yield s

    def find_larger_then(self, size):
        g = self.A141481()
        i = next(g)
        while i < size:
            i = next(g)

        return i


class Day3Test(TestCase):
    def setUp(self):
        self.day = Day3()

    def test_basic(self):
        self.assertEqual(self.day.calculate_distance(1), 0)
        self.assertEqual(self.day.calculate_distance(2), 1)
        self.assertEqual(self.day.calculate_distance(3), 2)
        self.assertEqual(self.day.calculate_distance(4), 1)
        self.assertEqual(self.day.calculate_distance(5), 2)
        self.assertEqual(self.day.calculate_distance(6), 1)
        self.assertEqual(self.day.calculate_distance(7), 2)
        self.assertEqual(self.day.calculate_distance(8), 1)
        self.assertEqual(self.day.calculate_distance(9), 2)
        self.assertEqual(self.day.calculate_distance(10), 3)
        self.assertEqual(self.day.calculate_distance(11), 2)
        self.assertEqual(self.day.calculate_distance(12), 3)
        self.assertEqual(self.day.calculate_distance(23), 2)
        self.assertEqual(self.day.calculate_distance(1024), 31)

    def test_generator_part2(self):
        a141481 = self.day.A141481()
        self.assertEqual(next(a141481), 1)
        self.assertEqual(next(a141481), 2)
        self.assertEqual(next(a141481), 4)
        self.assertEqual(next(a141481), 5)
        self.assertEqual(next(a141481), 10)
        self.assertEqual(next(a141481), 11)
        self.assertEqual(next(a141481), 23)
        self.assertEqual(next(a141481), 25)
        self.assertEqual(next(a141481), 26)
        self.assertEqual(next(a141481), 54)

    def test_puzzle(self):
        self.assertEqual(self.day.calculate_distance(self.puzzle()), 326)

    def test_puzzle_part2(self):
        self.assertEqual(self.day.find_larger_then(self.puzzle()), 363010)

    def puzzle(self):
        return 361527
