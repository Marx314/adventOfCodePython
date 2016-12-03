import json


class Day12(object):
    def __init__(self):
        self.ignore = None

    def sum(self, instructions, ignore=None):
        self.ignore = ignore
        instructions = json.loads(instructions)
        return self.process_loop(instructions.values())

    def process_loop(self, instructions):
        return sum([self.process(e) for e in instructions])

    def process(self, e):
        bling = 0
        if isinstance(e, dict) and self.ignore not in e.values():
            bling += self.process_loop(e.values())
        if isinstance(e, list):
            return self.process_loop(e)
        if isinstance(e, float) or isinstance(e, int):
            bling += e
        return bling
