TRAP = '^'
SAFE = '.'
TRAPS = [[TRAP, TRAP, SAFE], [SAFE, TRAP, TRAP], [TRAP, SAFE, SAFE], [SAFE, SAFE, TRAP]]


class Day18(object):
    @staticmethod
    def calculate_safe_tiles(row, row_count=10):
        count = row.count(SAFE)
        for i in range(1, row_count):
            row = Day18.get_next_row(row)
            count += row.count(SAFE)
        return count

    @staticmethod
    def get_next_row(row):
        left, center, right = Day18.get_left_tile(row)
        next_row = TRAP if Day18.is_a_trap(left, center, right) else SAFE

        for i in range(1, len(row) - 1):
            next_row += TRAP if Day18.is_a_trap(row[i - 1], row[i], row[i + 1]) else SAFE

        left, center, right = Day18.get_right_tile(row)
        next_row += TRAP if Day18.is_a_trap(left, center, right) else SAFE

        return next_row

    @staticmethod
    def get_right_tile(row):
        return row[-2], row[-1], SAFE

    @staticmethod
    def get_left_tile(row):
        return SAFE, row[0], row[1]

    @staticmethod
    def is_a_trap(left, center, right):  # Faster than any([..])!
        if left is TRAP and center is TRAP and right is not TRAP:
            return True
        if left is not TRAP and center is TRAP and right is TRAP:
            return True
        if left is TRAP and center is not TRAP and right is not TRAP:
            return True
        if left is not TRAP and center is not TRAP and right is TRAP:
            return True
        return False
