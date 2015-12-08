import re
from src.InputFetcher import InputFetcher


class Day5:
    def __init__(self):
        pass

    def nice(self, keys):
        count = 0
        vowels = "aeiou"
        bad_sequences = ['ab', 'cd', 'pq', 'xy']
        for string in keys:
            vowels_count = 0
            double_letter = 0
            bad_seq = 0
            for vowel in vowels:
                vowels_count += string.count(vowel)

            for letter in set(string):
                if letter*2 in string:
                    double_letter += 1
            for bad_sequence in bad_sequences:
                if bad_sequence in string:
                    bad_seq += 1

            if vowels_count >= 3 and double_letter > 0 and bad_seq == 0:
                count += 1

        return count

    def niceToo(self, strings):
        count = 0
        for string in strings:
            legal_pair = self._legal_pair(string)
            twice = self._twice_with_one_letter_between_them(string)
            if legal_pair and twice:
                count += 1

        return count

    def _legal_pair(self, string):
        pairs = list(set([string[i:i+2] for i in range(0, len(string)-1)]))
        for pair in pairs:
            if string.count(pair) > 1:
                return True
        return False

    def _twice_with_one_letter_between_them(self, string):
        letters = list(set(string))
        for letter in letters:
            pattern = "\A\w*[{0}][a-z][{0}]\w*$".format(letter)
            result = re.search(pattern, string)
            if string.count(letter) >= 2 and result is not None:
                return True

        return False

    @staticmethod
    def run():
        data = InputFetcher.fetch_input(5).split('\n')
        day = Day5()
        print data
        print day.nice(data)
        print day.niceToo(data)

