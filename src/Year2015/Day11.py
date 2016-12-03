import re


class Day11(object):
    def is_valid(self, password):
        two_pair = self.third_requirement(password)
        no_iol = self.second_requirement(password)
        lol = self.first_requirement(password)

        return two_pair and no_iol and lol

    def generate(self, password):
        password = self._replace_iol(password)
        return self._generate_next(password, len(password) - 1)

    def _replace_iol(self, password):
        i = None
        if 'i' in password:
            i = password.index('i')
        if 'o' in password:
            if i > password.index('o'):
                i = password.index('o')
        if 'l' in password:
            if i > password.index('l'):
                i = password.index('l')
        if i is not None:
            password = password[:i] + chr(ord(password[i]) + 1) + ('a' * len(password[i + 1:]))

        return password

    def _generate_next(self, password, chr):
        password = self._increment_char(password, chr)
        while not self.is_valid(password):
            password = self._increment_char(password, chr)
        return password

    def third_requirement(self, password):
        group = [m.group() for m in re.finditer(r'((\w)\2)+', password)]
        two_pair = True if len(group) >= 2 or (len(group) >= 1 and len(group[0]) >= 4) else False
        return two_pair

    def second_requirement(self, password):
        no_iol = False if 'i' in password or 'o' in password or 'l' in password else True
        return no_iol

    def first_requirement(self, password):
        bytes = [ord(x) for x in password]
        lol = [True for i in range(len(bytes) - 3) if
               bytes[i] + 2 == bytes[i + 1] + 1 and bytes[i + 1] + 1 == bytes[i + 2]]
        return len(lol) > 0

    def _increment_char(self, password, index):
        increment = False
        while increment is False:
            for i in range(index, 0, -1):
                if ord(password[i]) + 1 in range(ord('a'), ord('z') + 1):
                    password = password[:i] + chr(ord(password[i]) + 1) + password[i + 1:]
                    increment = True
                    break
                else:
                    password = password[:i] + 'a' + password[i + 1:]
        return password
