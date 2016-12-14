import hashlib
import re


class Day14(object):
    @staticmethod
    def one_time_pads(starting_key, required_keys, hashing_algorithm):
        hash_found = set()
        triple_regex = r'(.)\1\1'
        last_1000_triples = {}
        i = 0
        while len(hash_found) < required_keys:
            digest = hashing_algorithm("{0}{1}".format(starting_key, i))
            indexes = [index for index, value in last_1000_triples.items() if value in digest]
            if indexes:
                hash_found = hash_found.union(indexes)
            triple = re.findall(triple_regex, digest)
            if triple:
                last_1000_triples[i] = ''.join([triple[0] for _ in range(5)])
            Day14.remove_past_thousands_index(i, last_1000_triples)
            i += 1
        return sorted(hash_found)

    @staticmethod
    def remove_past_thousands_index(i, last_1000_triples):
        unset = [key for key in last_1000_triples.keys() if key + 1000 < i]
        if unset:
            for key in unset:
                del last_1000_triples[key]

    @staticmethod
    def simple_md5(key):
        return hashlib.md5(key.encode('utf-8')).hexdigest()

    @staticmethod
    def hash_2016(starting_key):
        count = 2016
        digest = hashlib.md5(starting_key.encode('utf-8')).hexdigest().encode('utf-8')
        while count > 0:
            digest = hashlib.md5(digest).hexdigest().encode('utf-8')
            count -= 1
        return digest.decode('utf-8')
