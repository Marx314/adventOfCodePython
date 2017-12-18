from collections import defaultdict
from unittest import TestCase

from src import split_data


@split_data
def execute_assembly(lines):
    register = defaultdict(lambda: 0)
    last_played_sound = 0
    position = 0
    while position < len(lines):
        line = lines[position].split(' ')
        if line[0] in ('set', 'add', 'mul', 'mod'):
            _execute_numeric_handling_assembly(line, register)
        elif line[0] == 'snd':
            last_played_sound = get_value(register, line[1])
        elif line[0] == 'rcv':
            if register[line[1]] != 0:
                return last_played_sound
        elif line[0] == 'jgz':
            if register[line[1]] > 0:
                position += get_value(register, line[2])
                continue
        position += 1


def _execute_numeric_handling_assembly(line, register):
    if line[0] == 'set':
        register[line[1]] = get_value(register, line[2])
    elif line[0] == 'add':
        register[line[1]] += get_value(register, line[2])
    elif line[0] == 'mul':
        register[line[1]] *= get_value(register, line[2])
    elif line[0] == 'mod':
        register[line[1]] %= get_value(register, line[2])


@split_data
def execute_duet(input):
    shared_bus = defaultdict(list)
    running = True
    register0 = defaultdict(lambda: 0)
    register1 = defaultdict(lambda: 0)
    register0['p'] = 0
    register1['p'] = 1
    position_0 = 0
    position_1 = 0
    while running:
        position_0 = _execute_thread_assembly(input, 0, register0, shared_bus, position_0)
        position_1 = _execute_thread_assembly(input, 1, register1, shared_bus, position_1)
        if shared_bus[0] == [] and shared_bus[1] == []:
            running = False
    return len(shared_bus['1 sent'])


def _execute_thread_assembly(lines, program_number, register, shared_bus, position=0):
    while position < len(lines):
        line = lines[position].split(' ')
        if line[0] in ('set', 'add', 'mul', 'mod'):
            _execute_numeric_handling_assembly(line, register)
        elif line[0] == 'snd':
            shared_bus[program_number].append(get_value(register, line[1]))
            shared_bus['{} sent'.format(program_number)].append(get_value(register, line[1]))
        elif line[0] == 'rcv':
            if len(shared_bus[(program_number + 1) % 2]):
                value = shared_bus[(program_number + 1) % 2].pop(0)
                register[line[1]] = value
            else:
                return position
        elif line[0] == 'jgz':
            if get_value(register, line[1]) > 0:
                position += get_value(register, line[2])
                continue
        position += 1


def get_value(register, value):
    if value in register:
        return register[value]
    return int(value)


class Day18Test(TestCase):
    def test_simple_dance(self):
        simple = '''set a 1
add a 2
mul a a
mod a 5
snd a
set a 0
rcv a
jgz a -1
set a 1
jgz a -2'''
        self.assertEqual(execute_assembly(simple), 4)

    def test_simple_part2(self):
        simple = '''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''

        self.assertEqual(execute_duet(simple), 3)

    def test_puzzle(self):
        self.assertEqual(execute_assembly(self.puzzle()), 4601)
        self.assertEqual(execute_duet(self.puzzle()), 6858)

    def puzzle(self):
        return '''set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 952
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19'''
