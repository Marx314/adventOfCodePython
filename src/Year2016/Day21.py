from collections import deque
from itertools import permutations
import re
from src import split_data

__author__ = 'maubry'


class Day21(object):
    def brute_force_password(self, instructions, expected_password):
        possibilities = permutations(expected_password)
        valid_password = []
        for password in possibilities:
            scrambled = self.scramble(instructions, password=password)
            if scrambled == expected_password:
                valid_password.append(''.join(password))
        return valid_password

    @split_data
    def scramble(self, instructions, password):
        for instruction in instructions:
            password = self.scramble_instruction(instruction, password)
        return password

    def scramble_instruction(self, instruction, password):
        password = list(password)
        if instruction.startswith('swap'):
            pos_x, pos_y = self._find_swap_position(instruction, password)
            password[pos_x], password[pos_y] = password[pos_y], password[pos_x],
        elif instruction.startswith('reverse'):
            pos_x, pos_y = map(int, re.findall('(\d+)', instruction))
            pos_y += 1
            password[pos_x:pos_y] = password[pos_x:pos_y][::-1]
        elif instruction.startswith('rotate'):
            side = self._find_rotation_side(instruction, password)
            password = deque(password)
            password.rotate(side)
        elif instruction.startswith('move'):
            pos_x, pos_y = map(int, re.findall('(\d+)', instruction))
            letter = password[pos_x]
            del password[pos_x]
            if pos_y >= len(password):
                password.append('')
            password[pos_y] = letter + password[pos_y]

        return ''.join(password)

    @staticmethod
    def _find_swap_position(instruction, password):
        if len(re.findall('(\d+)', instruction)) == 2:
            pos_x, pos_y = map(int, re.findall('(\d+)', instruction))
        else:
            letter_x, letter_y = re.findall('swap letter (\w) with letter (\w)', instruction)[0]
            pos_x, pos_y = password.index(letter_x), password.index(letter_y)
        return pos_x, pos_y

    @staticmethod
    def _find_rotation_side(instruction, password):
        if 'left' in instruction:
            return list(map(int, re.findall('(\d+)', instruction)))[0] * -1
        elif 'right' in instruction:
            return list(map(int, re.findall('(\d+)', instruction)))[0]
        else:
            letter = re.findall('letter (\w)', instruction)[0]
            n = password.index(letter)
            if n >= 4:
                n += 1
            return n + 1