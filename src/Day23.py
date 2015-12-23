from src import split_data


class Day23:
    def __init__(self, register):
        self.register = register

    @split_data
    def program(self, instructions):
        next_position = 0
        while next_position < len(instructions):
            i = instructions[next_position].split(' ')
            next_position = self.apply_instruction(i, i[0], next_position)

        return self.register

    def apply_instruction(self, i, command, position):
        if command == 'inc':
            self.register[i[1][0:1]] += 1
            position += 1
        elif command == 'hlf':
            self.register[i[1][0:1]] /= 2
            position += 1
        elif command == 'tpl':
            self.register[i[1][0:1]] *= 3
            position += 1
        elif command == 'jmp':
            position += int(i[1])
        elif command == 'jio' and self.register[i[1][0:1]] == 1:
            position += int(i[2])
        elif command == 'jie' and self.register[i[1][0:1]] % 2 == 0:
            position += int(i[2])
        else:
            position += 1
        return position
