from unittest import TestCase


def stronguest(raw_components):
    solutions = a(raw_components)
    sorted_solutions = sorted(solutions, key=lambda solution: sum([component[0] + component[1] for component in solution]))
    return score(sorted_solutions.pop())


def score(solution):
    return sum([component[0] + component[1] for component in solution])


def longuest(raw_components):
    solutions = a(raw_components)
    l = sorted(solutions, key=lambda solution: len(solution))
    return score(l.pop())


def a(raw_components):
    components = []
    for raw_component in raw_components.split('\n'):
        components.append(tuple(map(int, raw_component.split('/'))))

    return find_solutions(components, 0)


def find_solutions(components, initial):
    solutions = []
    for component in components:
        if initial in component:
            solutions.append([component])

            for solution in find_solutions([c for c in components if c is not component], component[1] if component[0] == initial else component[0]):
                solution.insert(0, component)
                solutions.append(solution)

    return solutions


class DayTest(TestCase):
    def test_simple_test(self):
        self.assertEqual(stronguest(self.simple_data()), 31)

    def test_simple_test_long(self):
        self.assertEqual(longuest(self.simple_data()), 19)

    def test_puzzle_high_score(self):
        self.assertEqual(stronguest(self.puzzle()), 2006)

    def test_puzzle_long(self):
        self.assertEqual(longuest(self.puzzle()), 1994)

    def simple_data(self):
        return '''0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10'''

    def puzzle(self):
        return '''24/14
30/24
29/44
47/37
6/14
20/37
14/45
5/5
26/44
2/31
19/40
47/11
0/45
36/31
3/32
30/35
32/41
39/30
46/50
33/33
0/39
44/30
49/4
41/50
50/36
5/31
49/41
20/24
38/23
4/30
40/44
44/5
0/43
38/20
20/16
34/38
5/37
40/24
22/17
17/3
9/11
41/35
42/7
22/48
47/45
6/28
23/40
15/15
29/12
45/11
21/31
27/8
18/44
2/17
46/17
29/29
45/50'''
