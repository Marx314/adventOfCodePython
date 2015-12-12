import hashlib


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

