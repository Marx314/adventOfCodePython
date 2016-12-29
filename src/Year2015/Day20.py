import functools
from sympy import divisors


@functools.lru_cache(maxsize=0)
def _(n):
    return divisors(n)


def calculate_house_sympy(house):
    return sum(_(house)) * 10


def houses_of_cards(house):
    gift_count = [0 for _ in range(house + 1)]
    for i in range(1, house + 1):
        gift_count[i] = calculate_house_sympy(i)
    return gift_count[1:]


def houses_of_cards_sum(max_gift_count, starting_at=1):
    for i in range(starting_at, max_gift_count):
        result = calculate_house_sympy(i)
        if result >= max_gift_count:
            return i


class Day20(object):
    def __init__(self):
        self.elf_per_house = {}

    def calculate_house_sympy_fifty(self, house):
        d = [self.count_elf(i) for i in _(house)]
        return sum(d) * 11

    def houses_of_cards_sum_fifty(self, max_gift_count, starting_at):
        for i in range(starting_at, max_gift_count):
            if self.calculate_house_sympy_fifty(i) >= max_gift_count:
                return i

    def count_elf(self, i):
        if i not in self.elf_per_house:
            self.elf_per_house[i] = 0
        elif self.elf_per_house[i] >= 50:
            return 0
        self.elf_per_house[i] += 1
        return i
