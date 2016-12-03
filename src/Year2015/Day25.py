import operator


def accumulate(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


class Day25(object):
    def __init__(self):
        pass

    def generate(self, row, col, start):
        position = self.get_position(col, row)
        return (int(start) * pow(252533, (position - 1), 33554393)) % 33554393

        #    |  1   2   3   4   5   6
        # ---+---+---+---+---+---+---+
        # 1 |  1   3   6  10  15  21
        # 2 |  2   5   9  14  20
        # 3 |  4   8  13  19
        # 4 |  7  12  18
        # 5 | 11  17
        # 6 | 16

    def get_position(self, col, row):
        side_length = row + col - 1
        area = side_length * (side_length + 1) / 2  # b*h/2
        position = area - row + 1
        return int(position)
