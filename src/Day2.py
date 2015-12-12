from src import split_data


class Day2:
    def __init__(self):
        pass

    @split_data
    def calc(self, data):
        result = [list(map(int, i.split('x'))) for i in data[:-1]]
        sq2 = [2 * i[0] * i[1] + 2 * i[1] * i[2] + 2 * i[0] * i[2] + min(i[0] * i[1], i[1] * i[2], i[0] * i[2]) for i in
               result]
        return sum(sq2)

    @split_data
    def ribbon(self, data):
        result = [list(map(int, i.split('x'))) for i in data[:-1]]
        length = 0
        for present_size in result:
            bow = present_size[0] * present_size[1] * present_size[2]
            present_size.remove(max(present_size))
            wrap = 2 * sum(present_size)
            length += bow + wrap
        return length
