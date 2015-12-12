import re
from src import split_data


class Day7:
    _instruction_pattern = r'^(?:(\w+)\s){0,1}(\w+)\s(?:(\w+)\s(\w+)\s){0,1}(\-\>)\s(\w+)'
    _MAX_INT = 65535

    def __init__(self):
        pass

    def calc(self, instructions):
        result = self.apply_operations(instructions)
        return result['a']

    def calc_b(self, instructions):
        instructions = instructions.replace('1674 -> b', '46065 -> b')
        return self.calc(instructions)

    @split_data
    def apply_operations(self, instructions):
        un_executed_instructions = []
        operation = {}
        self._execute_pass(instructions, operation, un_executed_instructions)
        count = 0
        max_repeat = len(instructions)
        while len(un_executed_instructions) > 0:
            if count == max_repeat:
                raise YOLO('You Obviouly Lived Old enough!')
            instructions = un_executed_instructions
            un_executed_instructions = []
            self._execute_pass(instructions, operation, un_executed_instructions)
            count += 1

        return operation

    def _execute_pass(self, instructions, operation, un_executed_instructions):
        for instruction in instructions:
            result = re.split(self._instruction_pattern, instruction)
            value = None
            if result[1] == 'NOT':
                if result[2] in operation:
                    value = self._MAX_INT - operation[result[2]]
            else:
                if result[3] == 'AND':
                    if result[2].isalpha() and result[2] in operation and result[4] in operation:
                        value = operation[result[2]] & operation[result[4]]
                    if result[2].isdecimal() and result[4] in operation:
                        value = int(result[2]) & operation[result[4]]
                elif result[3] == 'OR':
                    if result[2] in operation and result[4] in operation:
                        value = operation[result[2]] | operation[result[4]]
                elif result[3] == 'LSHIFT':
                    if result[2] in operation:
                        value = operation[result[2]] << int(result[4])
                elif result[3] == 'RSHIFT':
                    if result[2] in operation:
                        value = operation[result[2]] >> int(result[4])
                else:
                    if result[2].isalpha():
                        if result[2] in operation:
                            value = operation[result[2]]
                    else:
                        value = int(result[2])
            if value is not None:
                operation[result[6]] = value
            else:
                un_executed_instructions.append(instruction)


class YOLO(Exception):
    pass
