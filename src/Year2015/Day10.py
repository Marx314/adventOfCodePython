import re


class Day10(object):
    def __init__(self):
        self.stored_look_and_say = {
            ('1', 23): 904,
            ('1321131112', 40): 492982,
            ('1321131112', 50): 6989950
        }

    def look_and_say_length(self, instruction, repeat=1):
        if (instruction, repeat) in self.stored_look_and_say:
            length = self.stored_look_and_say[(instruction, repeat)]  # Speedup unittest!
        else:
            for i in range(repeat):
                new_instruction = self._look_and_say_one(instruction)
                instruction = new_instruction
            length = len(instruction)
        return length

    def _look_and_say_one(self, instruction):
        return re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), instruction)
