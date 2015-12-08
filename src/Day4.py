import hashlib
from src.InputFetcher import InputFetcher


class Day4:
    def __init__(self):
        pass

    def calc(self, key, n=5):
        result = 0
        zeros = "0"*n
        for i in xrange(100000000):
            digest = hashlib.md5("{0}{1}".format(key, i)).hexdigest()
            if digest[0:n] == zeros:
                result = i
                break

        return str(result)

    def calc6(self, key):
        return self.calc(key, n=6)

    @staticmethod
    def run():
        data = InputFetcher.fetch_input(4).split('\n')
        day = Day4()
        print data
        print day.calc(data)
        print day.calc6(data)

