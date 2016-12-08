from collections import deque
from src import split_data


class Day8(object):
    @split_data
    def calc(self, cmds, line=3, column=7):
        result = self.process_commands(cmds, column, line)

        return result

    @split_data
    def calc_on(self, cmds, line=3, column=7):
        result = self.process_commands(cmds, column, line)

        flatten = lambda l: [item for sublist in l for item in sublist]
        flatten_map = flatten(result)

        return flatten_map.count('#')

    def process_commands(self, cmds, column, line):
        lcd = self.init_map(line, column)
        for cmd in cmds:
            lcd = self.process_command(cmd, lcd)
        result = self.build_output(lcd)
        return result

    @staticmethod
    def build_output(lcd):
        result = ''
        for i in range(len(lcd)):
            result += ''.join(lcd[i])
            result += '\n'
            print(list(lcd[i]))
        return result[:-1]

    @staticmethod
    def process_command(cmd, lcd):
        if cmd.startswith('rect'):
            command = cmd.split(' ')
            y, x = command[1].split('x')
            for i in range(int(x)):
                for j in range(int(y)):
                    lcd[i][j] = '#'

        elif cmd.startswith('rotate column'):
            command = cmd.split(' ')
            column = int(command[2][2:])
            down = int(command[4])
            initial = deque([lcd[i][column] for i in range(len(lcd))])
            initial.rotate(down)
            for i in range(len(lcd)):
                lcd[i][column] = initial[i]

        elif cmd.startswith('rotate row'):
            command = cmd.split(' ')
            line = int(command[2][2:])
            right = int(command[4])
            initial = deque([lcd[line][i] for i in range(len(lcd[line]))])
            initial.rotate(right)
            lcd[line] = list(initial)

        return lcd

    @staticmethod
    def init_map(line, column):
        lcd = []
        for i in range(line):
            lcd.append([])
            for j in range(column):
                lcd[i].append('.')
        return lcd
