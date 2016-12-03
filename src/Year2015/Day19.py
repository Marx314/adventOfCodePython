import re
from src import split_data


class Day19(object):
    def __init__(self):
        pass

    @split_data
    def possibilities(self, instructions):
        expected_molecule = instructions.pop()
        instructions.pop()
        cell = self.generate_all_molecule(expected_molecule, instructions)

        return len(cell)

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

    def get_index_on_count(self, expected_molecule, src, count):
        i = 0
        pos = 0
        pattern = re.compile(src)
        for m in pattern.finditer(expected_molecule):
            if i == count:
                pos = m.start()
                break
            i += 1

        return pos

    @split_data
    def minimal_step_to(self, replacements, expected_molecule):
        step = 0
        steps = []
        cells = self.generate_all_molecule('e', replacements)
        if expected_molecule in cells:
            steps.append(step)
        for cell in cells:
            self.apply_steps(expected_molecule, cell, replacements, step + 1, steps)

        return min(steps)

    def apply_steps(self, expected_molecule, source_molecule, replacements, step, steps):
        new_cells = self.generate_all_molecule(source_molecule, replacements)
        if expected_molecule in new_cells:
            steps.append(step + 1)
        else:
            for cell in new_cells:
                if len(cell) <= len(expected_molecule):
                    self.apply_steps(expected_molecule, cell, replacements, step + 1, steps)

    @split_data
    def minimal_step_to_puzzle(self, replacements):
        expected_molecule = replacements.pop()
        replacements.pop()
        step = 0
        steps = []
        cells = self.generate_all_molecule('e', replacements)
        if expected_molecule in cells:
            steps.append(step)
        cells = ['HF']
        for cell in cells:
            self.apply_steps(expected_molecule, cell, replacements, step + 1, steps)

        return min(steps)
