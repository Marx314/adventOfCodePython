from src import split_data


class Day20(object):
    @split_data
    def lowest_allowed_ip(self, rules):
        blocked_ranges = sorted([list(map(int, rule.split('-'))) for rule in rules], key=lambda x: x[0])
        blocked_ranges = self._get_non_overlapping_range(blocked_ranges)
        return blocked_ranges[0][1] + 1

    @split_data
    def count_allowed_ip(self, rules):
        blocked_ranges = sorted([list(map(int, rule.split('-'))) for rule in rules], key=lambda x: x[0])
        blocked_ranges = self._get_non_overlapping_range(blocked_ranges)
        allowed = [len(range(blocked_ranges[i][1], blocked_ranges[i + 1][0] + 1)) for i in
                   range(len(blocked_ranges) - 1)]
        return len(allowed)

    @staticmethod
    def _get_non_overlapping_range(blocked_ranges):
        i = 0
        while i < len(blocked_ranges) - 1:
            if blocked_ranges[i][1] + 1 >= blocked_ranges[i + 1][0]:
                blocked_ranges.append([blocked_ranges[i][0], max(blocked_ranges[i][1], blocked_ranges[i + 1][1])])
                del blocked_ranges[i + 1]
                del blocked_ranges[i]
                blocked_ranges = sorted(blocked_ranges, key=lambda x: x[0])
                i = 0
            else:
                i += 1
        return blocked_ranges
