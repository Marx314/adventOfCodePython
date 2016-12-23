from src import split_data

REPLACEMENTS = {'inc': 'dec', 'dec': 'inc', 'jnz': 'cpy', 'cpy': 'jnz', 'tgl': 'inc'}


class Day23(object):
    register = None

    @split_data
    def program(self, instructions, register):
        self.register = register
        next_position = 0
        while next_position < len(instructions):
            i = instructions[next_position].split(' ')
            next_position = self.apply_instruction(i, i[0], next_position, instructions)

        return self.register

    def apply_instruction(self, i, command, position, instructions):
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
        elif command == 'tgl' and i[1] in self.register:
            next_position = self.register[i[1]] + position
            if next_position < len(instructions):
                self.apply_toggle(next_position, instructions)
        position += 1
        return position

    @staticmethod
    def apply_toggle(next_position, instructions):
        i = instructions[next_position].split(' ')
        i[0] = REPLACEMENTS[i[0]]
        instructions[next_position] = ' '.join(i)
