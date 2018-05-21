import re
from collections import defaultdict
from unittest import TestCase


def diagnostic(blueprint):
    state_machine = {}
    current_state = ''
    line_number = 0
    instruction = blueprint.split('\n')
    steps = 0
    while line_number < len(instruction):
        line = instruction[line_number]
        if "Begin in state" in line:
            current_state = line[-2]
            line_number += 1
        elif "Perform a diagnostic" in line:
            steps = int(re.findall('(\d+)', line)[0])
            line_number += 1
        elif "In state" in line:
            current_state = line[-2]
            state_machine[current_state] = {0: {'value': 0, 'index': 0, 'state': 'A'}, 1: {'value': 0, 'index': 0, 'state': 'A'}}
            if "Write the value 1" in instruction[line_number + 2]:
                state_machine[current_state][0]['value'] = 1
            else:
                state_machine[current_state][0]['value'] = 0
            if "Move one slot to the right" in instruction[line_number + 3]:
                state_machine[current_state][0]['index'] = 1
            else:
                state_machine[current_state][0]['index'] = -1
            state_machine[current_state][0]['state'] = instruction[line_number + 4][-2]
            if "Write the value 1" in instruction[line_number + 6]:
                state_machine[current_state][1]['value'] = 1
            else:
                state_machine[current_state][1]['value'] = 0
            if "Move one slot to the right" in instruction[line_number + 7]:
                state_machine[current_state][1]['index'] = 1
            else:
                state_machine[current_state][1]['index'] = -1
            state_machine[current_state][1]['state'] = instruction[line_number + 8][-2]
            line_number += 8
        else:
            line_number += 1

    memory = defaultdict(lambda :0)
    index = 0
    for i in range(steps):
        state = state_machine[current_state][memory[index]]
        memory[index] = state['value']
        index += state['index']
        current_state = state['state']
    return sum(memory.values())


class DayTest(TestCase):
    def test_simple_test(self):
        blueprint = '''Begin in state A.
Perform a diagnostic checksum after 6 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.'''
        self.assertEqual(diagnostic(blueprint), 3)

    def test_puzzle(self):
        # less then 12172063
        self.assertEqual(diagnostic(self.puzzle()), 1670)

    def puzzle(self):
        return '''Begin in state A.
Perform a diagnostic checksum after 12172063 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state C.

In state D:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state E.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state F.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.'''
