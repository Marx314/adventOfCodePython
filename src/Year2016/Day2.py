VOID = '0'


class Day2(object):
    def find_seq(self, pad, sequences, position=[1, 1]):
        result = ''
        for sequence in sequences.split('\n'):
            for letter in sequence:
                if letter == 'U':
                    if position[0] >= 1:
                        if pad[position[0] - 1][position[1]] != VOID:
                            position[0] -= 1
                if letter == 'D':
                    if position[0] < len(pad) - 1:
                        if pad[position[0] + 1][position[1]] != VOID:
                            position[0] += 1
                if letter == 'L':
                    if position[1] >= 1:
                        if pad[position[0]][position[1] - 1] != VOID:
                            position[1] -= 1
                if letter == 'R':
                    if position[1] < len(pad[position[0]]) - 1:
                        if pad[position[0]][position[1] + 1] != VOID:
                            position[1] += 1
            result = result + pad[position[0]][position[1]]
        return result
