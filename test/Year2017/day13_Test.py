from unittest import TestCase

from src import split_data


@split_data
def get_severity(firewall_rules):
    firewall = build_rules(firewall_rules)

    severity = {layer: cycle for layer, cycle in firewall.items() if (layer % ((cycle - 1) * 2)) == 0}

    return sum([k * v for k, v in severity.items()])


def build_rules(firewall_rules):
    firewall = {}
    for rule in firewall_rules:
        depth, cycle = map(int, rule.split(':'))
        firewall[depth] = cycle
    return firewall


@split_data
def get_delay_to_pass_firewall(firewall_rules):
    firewall = build_rules(firewall_rules)

    delay = 1
    while not passing_all_rules(firewall, delay):
        delay += 1
    return delay


def passing_all_rules(firewall, delay):
    for layer, cycle in firewall.items():
        if ((layer + delay) % ((cycle - 1) * 2)) == 0:
            return False
    return True


class Day13Test(TestCase):
    def test_simple_program_list(self):
        sample = '''0: 3
1: 2
4: 4
6: 4'''
        self.assertEqual(get_severity(sample), 24)
        self.assertEqual(get_delay_to_pass_firewall(sample), 10)

    def test_puzzle(self):
        self.assertEqual(get_severity(self.puzzle()), 1728)
        self.assertEqual(get_delay_to_pass_firewall(self.puzzle()), 3946838)

    def puzzle(self):
        return '''0: 3
1: 2
2: 4
4: 8
6: 5
8: 6
10: 6
12: 4
14: 6
16: 6
18: 9
20: 8
22: 8
24: 8
26: 8
28: 10
30: 8
32: 12
34: 10
36: 14
38: 12
40: 12
42: 12
44: 12
46: 12
48: 12
50: 14
52: 12
54: 14
56: 12
58: 12
60: 14
62: 18
64: 14
68: 14
70: 14
72: 14
74: 14
78: 14
80: 20
82: 14
84: 14
90: 17'''
