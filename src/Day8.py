import re
from src.InputFetcher import InputFetcher


class Day8:

    def __init__(self):
        pass

    def calc(self, instructions):
        memory = 0
        literal = 0
        for instruction in instructions:
            memory += len(instruction)
            literal += len(eval(instruction))

        return memory - literal

    def encoded(self, instructions):
        encoded = 0
        literal = 0
        for instruction in instructions:
            encoded += len(re.escape(instruction))+2
            literal += len(instruction)
        return encoded - literal

    @staticmethod
    def run():
        data = InputFetcher.fetch_input(8).split('\n')
        day = Day8()
        print data
        print day.calc(data)
        print day.encoded(data)

