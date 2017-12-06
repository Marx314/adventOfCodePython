import copy
from unittest import TestCase

banks_to_string = lambda x: ' '.join(map(str, x))


class Day6:
    def cycle(self, bank):
        memory_banks = [int(i) for i in bank.split()]
        memory_banks_length = len(memory_banks)
        cycle = 0
        seen = []

        while memory_banks not in seen:
            seen.append(copy.copy(memory_banks))
            cycle += 1
            blocks = max(memory_banks)
            index = memory_banks.index(blocks)
            memory_banks[index] = 0
            while blocks > 0:
                index += 1
                memory_banks[index % memory_banks_length] += 1
                blocks -= 1

        return cycle, memory_banks, seen


class Day6Test(TestCase):
    def setUp(self):
        self.day = Day6()

    def test_simple_memory_cycle(self):
        memory_banks = '0 2 7 0'
        cycle, memory_banks, _ = self.day.cycle(memory_banks)
        self.assertEqual(cycle, 5)
        self.assertEqual(banks_to_string(memory_banks), '2 4 1 2')

    def test_simple_memory_cycle_part2(self):
        memory_banks = '0 2 7 0'
        cycle, memory_banks, seen = self.day.cycle(memory_banks)
        self.assertEqual(cycle - seen.index(memory_banks), 4)
        self.assertEqual(banks_to_string(memory_banks), '2 4 1 2')

    def test_puzzle(self):
        cycle, memory_banks, seen = self.day.cycle(self.puzzle())
        self.assertEqual(cycle, 3156)
        self.assertEqual(banks_to_string(memory_banks), '0 13 12 10 9 8 7 5 3 2 1 1 1 10 6 5')

        self.assertEqual(cycle - seen.index(memory_banks), 1610)

    def puzzle(self):
        return '''2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14'''
