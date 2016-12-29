import random
import re
from src import split_data


class Day19(object):
    @split_data
    def possibilities(self, instructions):
        expected_molecule = instructions.pop()
        instructions.pop()
        cell = self.generate_all_molecule(expected_molecule, instructions)

        return len(cell)

    @split_data
    def shortest_path_length(self, replacements):
        expected_molecule = replacements.pop()
        replacements.pop()
        instructions = self.get_instructions(replacements)
        count, replacing = self._find_random_solution_from_molecule_to_e(expected_molecule, instructions)
        first_src, first_dst = replacing[-1]
        while first_dst != 'e':
            count, replacing = self._find_random_solution_from_molecule_to_e(expected_molecule, instructions)
            first_src, first_dst = replacing[-1]

        return count

    @staticmethod
    def _find_random_solution_from_molecule_to_e(expected_molecule, instructions):
        replacing = []
        count = 0
        index = 0

        while index < len(instructions) and expected_molecule != 'e':
            src, dst = instructions[index]
            if src in expected_molecule:
                found_index = expected_molecule.index(src)
                expected_molecule = expected_molecule[0:found_index] + dst + expected_molecule[found_index + len(src):]
                replacing.append((src, dst))
                index = 0
                count += 1
                random.shuffle(instructions)
            else:
                index += 1
        return count, replacing

    @staticmethod
    def get_instructions(instructions_text):
        instructions = []
        for i in instructions_text:
            src, dst = i.split(' => ')
            instructions.append((dst, src))
        return instructions

    def generate_all_molecule(self, expected_molecule, instructions):
        cell = set()
        for i in instructions:
            stuff = i.split(' => ')
            src = stuff[0]
            dst = stuff[1]
            for j in range(len(expected_molecule)):
                if src in expected_molecule:
                    [cell.add(self._generate(src, dst, expected_molecule, count)) for count in
                     range(expected_molecule.count(src))]
        return cell

    def _generate(self, src, dst, expected_molecule, count):
        index = self.get_index_on_count(expected_molecule, src, count)
        size = len(src)
        l = list(expected_molecule)
        if size == 1:
            l[index] = dst
        if size == 2:
            l[index] = dst
            l[index + 1] = ''

        return ''.join(l)

    @staticmethod
    def get_index_on_count(expected_molecule, src, count):
        i = 0
        pos = 0
        pattern = re.compile(src)
        for m in pattern.finditer(expected_molecule):
            if i == count:
                pos = m.start()
                break
            i += 1

        return pos
