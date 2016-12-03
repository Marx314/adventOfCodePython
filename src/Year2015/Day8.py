import re
from src import split_data


class Day8(object):
    def __init__(self):
        pass

    @split_data
    def used_in_memory(self, instructions):
        memory = 0
        literal = 0
        for instruction in instructions:
            memory += len(instruction)
            literal += len(eval(instruction))

        return memory - literal

    @split_data
    def encoded_use_in_memory(self, instructions):
        encoded = 0
        literal = 0
        for instruction in instructions:
            encoded += len(re.escape(instruction)) + 2
            literal += len(instruction)
        return encoded - literal
