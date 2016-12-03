from src import split_data


class Day16(object):
    def __init__(self):
        self.attributes = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
        }

    @split_data
    def find_sue(self, instructions):
        sues = self._handle_sues(instructions)
        matching = [[] for _ in range(0, 501)]
        for n, sue in enumerate(sues):
            for attribute in sue.keys():
                self._apply_simple_attributes(attribute, matching[n + 1], sue)

        return [n for n, attributes in enumerate(matching) if len(attributes) == 3][0]

    @split_data
    def find_sue_issue(self, instructions):
        sues = self._handle_sues(instructions)
        matching = [[] for _ in range(0, 501)]
        for n, sue in enumerate(sues):
            for attribute in sue.keys():
                self._apply_attributes(attribute, matching[n + 1], sue)

        return [n for n, attributes in enumerate(matching) if len(attributes) == 3][0]

    def _apply_attributes(self, attribute, matching, sue):
        if attribute in ['cats', 'trees'] and sue[attribute] > self.attributes[attribute]:
            matching.append(attribute)
        elif attribute in ['pomeranians', 'goldfish'] and sue[attribute] < self.attributes[attribute]:
            matching.append(attribute)
        elif sue[attribute] == self.attributes[attribute]:
            matching.append(attribute)

    def _apply_simple_attributes(self, attribute, matching, sue):
        if sue[attribute] == self.attributes[attribute]:
            matching.append(attribute)

    def _handle_sues(self, instructions):
        return [self._handle_sue(instruction.split(' ')) for instruction in instructions]

    def _handle_sue(self, result):
        return {
            result[2][:-1]: int(result[3][:-1]),
            result[4][:-1]: int(result[5][:-1]),
            result[6][:-1]: int(result[7]),
        }
