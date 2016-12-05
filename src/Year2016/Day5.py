import hashlib


class Day5(object):
    def __init__(self):
        self.start = 0
        self.number_of_zero = 5
        self.index = 0

        self.precomputed = {
            'abc': {
                'last_start': 13753421,
                'hash': [
                    '00000155f8105dff7f56ee10fa9b9abd',
                    '000008f82c5b3924a1ecbebf60344e00',
                    '00000f9a2c309875e05c5a5d09f1b8c4',
                    '000004e597bd77c5cd2133e9d885fe7e',
                    '0000073848c9ff7a27ca2e942ac10a4c',
                    '00000a9c311683dbbf122e9611a1c2d4',
                    '000003c75169d14fdb31ec1593915cff',
                    '0000000ea49fd3fc1b2f10e02d98ee96',
                    '000006e42e097c536b8be5179d65f327',
                    '000007b9278b049b172742aa82b5119a',
                    '000009d6e11733ceb6566b9c925a0770',
                    '00000cf8353c7d266a990865ea529f26',
                    '00000d64ba3bbc8102ec6179e495d88e',
                    '000006601753bceae1d061b3600deb3e',
                    '0000058939cbc6a1d1ab3bf7d29b0764',
                    '000002af5a2d97ef50063c37644d0166'
                ]
            },
            'ojvtpuvg': {
                'last_start': 27649592,
                'hash': [
                    '000004c52f7523dcea0ae987bb4bb7ae',
                    '000005b6777c6a6a5a72d3593ee1bade',
                    '0000049c67c129f031d6d2712e3e011d',
                    '00000307d284ec5fe32c12546f61d675',
                    '00000c4b121a0b7dceb8f719e3e5b9d1',
                    '00000101e84b5e967cba0ba19c7e7e00',
                    '00000574e86e49ffc208b84e771f3487',
                    '00000439e8d28b6d251a65563b7c09d1',
                    '000008b0db39adef6a1d517303fea769',
                    '00000cf7dcf231d21fe7fdde75ddc435',
                    '00000bfdb76ea16ec5a2ebcab4e3ae0c',
                    '0000097dd5e65fd1437a5df439a4788a',
                    '0000025a843b2da11af739013e61606f',
                    '000004c59a9346e28b5874a9931665dd',
                    '000007d5f6040c1a402d7b5994b1e061',
                    '00000c85b6afcb3487bcf9dd25a8d397',
                    '0000015e5a89c4d43c138ec7216377f7',
                    '000005433f1e5cb8c968edd5809e23e8',
                    '00000daa272097f561153938c9156eb4',
                    '00000e828dc841618678aeed7a4af074',
                    '00000f0434b9dd57d34a30dd213e2227',
                    '000006b0b288f96dcfc18f6a2414968b',
                    '00000c434af05fa7a5ebe670b07c7c34',
                    '0000001c18c78b4ca1896ebc9692c67d'
                ]
            }

        }

    def find_next(self, door_id, length, start=0):
        self.start = start
        result = ''
        for i in range(length):
            character, position = self._find_next_character(door_id)
            result += character

        return result

    def find_position(self, door_id, length):
        result = {}
        while len(result) != length:
            character, position = self._find_next_character(door_id, 6)
            if position in [str(i) for i in range(length) if str(i) not in result.keys()]:
                result[position] = character
        return ''.join([result[str(i)] for i in range(length) if str(i) in result.keys()])

    def _find_next_character(self, door_id, index_character=5):
        zeros = "0" * self.number_of_zero
        if door_id in self.precomputed:
            if self.index < len(self.precomputed[door_id]['hash']):
                digest = self.precomputed[door_id]['hash'][self.index]
                character = digest[index_character]
                position = digest[index_character - 1]
                self.index += 1
                if self.index == len(self.precomputed[door_id]['hash']):
                    self.start = self.precomputed[door_id]['last_start'] + 1
            else:
                character, position = self._brute_force_hash(door_id, index_character, zeros)
        else:
            character, position = self._brute_force_hash(door_id, index_character, zeros)

        return character, position

    def _brute_force_hash(self, door_id, index_character, zeros):
        for i in range(self.start, 1000000000):
            digest = hashlib.md5("{0}{1}".format(door_id, i).encode('utf-8')).hexdigest()
            if digest[0:self.number_of_zero] == zeros:
                print(digest)
                character = digest[index_character]
                position = digest[index_character - 1]
                print("{0}{1}".format(door_id, i).encode('utf-8'))
                self.start = i + 1
                break
        return character, position
