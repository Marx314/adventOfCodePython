from src.InputFetcher import InputFetcher


class Day1:
    def __init__(self):
        pass

    def calc(self, data):
        return data.count('(') - data.count(')')

    def floor(self, data):
        i = 0
        count = 0
        for direction in data:
            if i == -1:
                break
            count += 1
            if direction == '(':
                i += 1
            else:
                i -= 1

        return count

    @staticmethod
    def run():
        data = InputFetcher.fetch_input(1)
        day = Day1()
        print data
        print day.calc(data)
        print day.floor(data)

Day1.run()
