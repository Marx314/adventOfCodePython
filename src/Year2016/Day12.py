from src import split_data


class Day12(object):
    register = None

    @split_data
    def program(self, instructions, register):
        self.register = register
        next_position = 0
        while next_position < len(instructions):
            i = instructions[next_position].split(' ')
            next_position = self.apply_instruction(i, i[0], next_position)

        return self.register

    def apply_instruction(self, i, command, position):
        if command == 'inc':
            self.register[i[1][0:1]] += 1
        elif command == 'dec':
            self.register[i[1][0:1]] -= 1
        elif command == 'cpy' and i[1] not in self.register:
            self.register[i[2]] = int(i[1])
        elif command == 'cpy' and i[1] in self.register:
            self.register[i[2]] = self.register[i[1]]
        elif command == 'jnz' and i[1] not in self.register and int(i[1]) != 0:
            position += int(i[2]) - 1
        elif command == 'jnz' and i[1] in self.register and self.register[i[1]] != 0:
            position += int(i[2]) - 1
        position += 1
        return position
