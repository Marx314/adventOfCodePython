from collections import Counter
from src import split_data


class Day6(object):
    def __init__(self):
        pass

    @split_data
    def get_repetition(self, input):
        col = self._get_column(input)
        result = ''
        for i in range(len(input[0])):
            result += Counter(col[i]).most_common(1)[0][0]
        return result

    @split_data
    def get_less_repetition(self, data):
        col = self._get_column(data)
        result = ''
        for i in range(len(data[0])):
            result += Counter(col[i]).most_common()[-1][0]
        return result

    @staticmethod
    def _get_column(data):
        col = {}
        for i in range(len(data[0])):
            col[i] = ''
        for i in range(len(data[0])):
            for line in data:
                col[i] += line[i]
        return col
