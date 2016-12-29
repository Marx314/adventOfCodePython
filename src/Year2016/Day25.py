import copy
from src import split_data

REPLACEMENTS = {'inc': 'dec', 'dec': 'inc', 'jnz': 'cpy', 'cpy': 'jnz', 'tgl': 'inc'}


class NoPatternFor(Exception):
    pass


class Found(Exception):
    pass


class Day25(object):
    register = None
    initial_register = None
    out = ''

    def validate_output(self, value):
        if len(self.out):
            if self.out[-1] == value:
                raise NoPatternFor(self.initial_register['a'])
        elif value != '0':
            raise NoPatternFor(self.initial_register['a'])
        if len(self.out) == 1000:
            raise Found(self.initial_register['a'])
        self.out = '{}{}'.format(self.out, value)

    @split_data
    def program(self, instructions, register):
        self.out = ''
        self.register = register
        self.initial_register = copy.deepcopy(register)
        next_position = 0
        while next_position < len(instructions):
            i = instructions[next_position].split(' ')
            next_position = self.apply_instruction(i, i[0], next_position)

        return self.register

    def apply_instruction(self, i, command, position):
        if command == 'inc':
            self.register[i[1]] += 1
        elif command == 'dec':
            self.register[i[1]] -= 1
        elif command == 'cpy':
            if i[1].isalpha():
                self.register[i[2]] = self.register[i[1]]
            else:
                self.register[i[2]] = int(i[1])
        elif command == 'jnz' and i[1].isdigit() and int(i[1]) != 0:
            if i[2].isalpha():
                position += self.register[i[2]] - 1
            else:
                position += int(i[2]) - 1
        elif command == 'jnz' and i[1] in self.register and self.register[i[1]] != 0:
            position += int(i[2]) - 1
        elif command == 'out' and i[1].isalpha():
            self.validate_output('{}'.format(self.register[i[1]]))
        elif command == 'out':
            self.validate_output(i[1])
        position += 1
        return position
