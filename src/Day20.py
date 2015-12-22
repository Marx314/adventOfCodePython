from sympy import divisors


class Day20:
    def __init__(self):
        self.elf_per_house = {}

    def houses_of_cards(self, house):
        gift_count = [0 for _ in xrange(house+1)]
        for i in xrange(1, house+1):
            gift_count[i] = self.calculate_house_sympy(i)
        return gift_count[1:]

    def calculate_house_sympy(self, house):
        return sum(divisors(house))*10

    def calculate_house_sympy_fifty(self, house):
        d = [self.count_elf(i) for i in divisors(house)]
        return sum(d)*11

    def houses_of_cards_sum(self, max_gift_count):
        for i in xrange(1, max_gift_count):
            result = self.calculate_house_sympy(i)
            if result >= max_gift_count:
                return i

    def houses_of_cards_sum_fifty(self, max_gift_count):
        for i in xrange(1, max_gift_count):
            result = self.calculate_house_sympy_fifty(i)
            if result >= max_gift_count:
                return i

    def count_elf(self, i):
        if i not in self.elf_per_house:
            self.elf_per_house[i] = 0
        elif self.elf_per_house[i] >= 50:
            return 0
        self.elf_per_house[i] += 1
        return i

