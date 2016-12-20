import math


class Day19(object):
    # https://www.wikiwand.com/en/Josephus_problem
    @staticmethod
    def get_elf_alive(elf_count):
        binary_of_elf_count = "{0:b}".format(elf_count)
        bin_representation = '{}1'.format(binary_of_elf_count[1:])
        winner = int(bin_representation, 2)
        return winner

    @staticmethod
    def get_elf_alive_killing_the_one_facing(elf_count):
        root = math.pow(3, math.floor(math.log(elf_count, 3)))
        over = elf_count - root
        if over == 0:
            return elf_count
        else:
            return min(root, over) + max(0, over - root) * 2
