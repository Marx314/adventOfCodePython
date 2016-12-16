class Day16(object):
    @staticmethod
    def generate_data(a):
        b = ''.join(list(reversed(a)))
        b = b.replace('0', '2')
        b = b.replace('1', '0')
        b = b.replace('2', '1')
        return a + '0' + b

    def generate_data_until(self, initial, length):
        result = self.generate_data(initial)
        while len(result) < length:
            result = self.generate_data(result)
        return result[0:length]

    def checksum(self, data):
        pair = [data[i:i + 2] for i in range(0, len(data), 2)]
        chk = ''.join(map(lambda x: '1' if x in ['00', '11'] else '0', pair))
        if len(chk) % 2 == 0:
            return self.checksum(chk)
        return chk
