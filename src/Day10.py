import re


class Day10:
    def __init__(self):
        pass

    def look_and_say_length(self, instruction, repeat=1):
        for i in xrange(repeat):
            new_instruction = self._look_and_say_one(instruction)
            instruction = new_instruction
        return len(instruction)

    def _look_and_say_one(self, instruction):
        return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), instruction)
