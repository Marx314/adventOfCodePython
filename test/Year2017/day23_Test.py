from collections import defaultdict
from unittest import TestCase

from src import split_data


@split_data
def execute_assembly(lines):
    register = defaultdict(lambda: 0)
    position = 0
    while position < len(lines):
        line = lines[position].split(' ')
        if line[0] == 'set':
            register[line[1]] = get_value(register, line[2])
        elif line[0] == 'sub':
            register[line[1]] -= get_value(register, line[2])
        elif line[0] == 'mul':
            register['mul'] += 1
            register[line[1]] *= get_value(register, line[2])
        elif line[0] == 'jnz':
            if get_value(register, line[1]) != 0:
                position += get_value(register, line[2])
                continue
        position += 1
    return register['mul']


def get_value(register, value):
    if value.isalpha():
        return register[value]
    return int(value)


@split_data
def execute_assemblya(lines):
    register = defaultdict(lambda: 0)
    register['a'] = 1
    position = 0
    initial = 'a=1\n' \
              'b, c, d, f, g, h = 0'
    code = []
    gotos = []
    for index, line in enumerate(lines):
        line = line.split(' ')
        if line[0] == 'set':
            code.append('{} = {}'.format(line[1], line[2]))
        elif line[0] == 'sub':
            code.append('{} -= {}'.format(line[1], line[2]))
        elif line[0] == 'mul':
            code.append('{} *= {}'.format(line[1], line[2]))
        elif line[0] == 'jnz':
            gotos.append(index + int(line[2]))
            code.append('if {} != 0:\n      line = {}\n      continue'.format(line[1], index + int(line[2])))
        position += 1
    print(initial)
    print('while True:')
    for index, c in enumerate(code):
        if index in gotos:
            print('    line = {}'.format(index))
            print('  if line == {}:'.format(index))
        print('    {}'.format(c))

    return code


def solve(part, instructions):
    registers = defaultdict(int)
    registers['a'] = part - 1
    interpret = lambda val: registers[val] if val.isalpha() else int(val)
    i = 0
    while i < 11:
        op, reg, val = instructions[i].split()
        if op == 'set':
            registers[reg] = interpret(val)
        elif op == 'sub':
            registers[reg] -= interpret(val)
        elif op == 'mul':
            registers[reg] *= interpret(val)
        elif op == 'jnz':
            if interpret(reg) != 0:
                i += interpret(val)
                continue
        i += 1

    if part == 1:
        return (registers['b'] - registers['e']) * (registers['b'] - registers['d'])
    else:
        nonprimes = 0
        for b in range(registers['b'], registers['c'] + 1, 17):
            if any(b % d == 0 for d in range(2, int(b ** 0.5))):
                nonprimes += 1
        return nonprimes


class DayTest(TestCase):
    def test_puzzle(self):
        self.assertEqual(execute_assembly(self.puzzle()), 1670)

    def test_puzzle_part2(self):
        self.assertEqual(execute_assemblya(self.puzzle()), 1670)

    def test_puzzle_part22(self):
        self.assertEqual(solve(2, self.puzzle().split('\n')), 1670)

    def puzzle(self):
        return '''set b 67
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''
