import re
from src import split_data


class Day7(object):
    @split_data
    def count_valid_tls(self, puzzles):
        supported = [self.valid_tls(i) for i in puzzles]
        return sum(supported)

    @split_data
    def count_valid_ssl(self, puzzles):
        supported = [self.valid_ssl(i) for i in puzzles]
        return sum(supported)

    def valid_tls(self, ipv7):
        result = self._split_ipv7(ipv7)
        legal = any([self._contain_abba(result[i]) for i in range(1, len(result), 2)])
        if legal:
            return False

        valid = any([self._contain_abba(result[i]) for i in range(0, len(result), 2)])

        return valid

    def valid_ssl(self, ipv7):
        result = self._split_ipv7(ipv7)
        abas = self.get_abas(result)
        for aba in abas:
            bab = ''.join([aba[1], aba[0], aba[1]])
            if any([result[i] for i in range(1, len(result), 2) if bab in result[i]]):
                return True
        return False

    def get_abas(self, result):
        abas = []
        for i in range(0, len(result), 2):
            if self._get_aba(result[i]):
                abas += self._get_aba(result[i])
        return abas

    def _split_ipv7(self, ipv7):
        hypernets = ipv7.count('[')
        regex = self._build_regex(hypernets)
        result = [i for i in re.split(regex, ipv7) if i != '']
        return result

    @staticmethod
    def _build_regex(hypernets):
        base = '(\w*)\[(\w*)\]'
        return ''.join([base for i in range(hypernets)] + ['(\w*)'])

    @staticmethod
    def _contain_abba(sup_ipv7):
        result = re.search(r'([a-z])([a-z])\2\1', sup_ipv7)
        if result:
            result = result.groups()
            return result[0] != result[1]
        return False

    @staticmethod
    def _get_aba(sub_ipv7):
        result = re.findall(r'(?=((.)(?!\2)(.)\2))', sub_ipv7)
        if result:
            return [i[0] for i in result]
        return None
