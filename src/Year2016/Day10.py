import re
from src import split_data


class Day10(object):
    def __init__(self):
        self.highlight = (2, 5)
        self.highlight_bot = None

    @split_data
    def process(self, instructions):
        bots = {}
        bins = {}
        self.build_bots_rules(bots, instructions)
        for instruction in instructions:
            if 'goes to bot' in instruction:
                value, bot = map(int, re.findall('\w*\d', instruction))
                self.give_to_bot(bots, bot, bins, value)

        return bins

    def build_bots_rules(self, bots, instructions):
        for instruction in instructions:
            if 'gives' in instruction:
                if instruction.count('bot') == 3:
                    bot, low_dest, high_dest = map(int, re.findall('\w*\d', instruction))
                    self.add_rule_bot(bots, bot, low_dest, 'min')
                    self.add_rule_bot(bots, bot, high_dest, 'max')
                elif instruction.count('output') == 2:
                    bot, low_dest, high_dest = map(int, re.findall('\w*\d', instruction))
                    self.add_rule_output(bots, bot, low_dest, 'min')
                    self.add_rule_output(bots, bot, high_dest, 'max')
                elif instruction.index('output') < instruction.index('bot', 1):
                    bot, low_dest, high_dest = map(int, re.findall('\w*\d', instruction))
                    self.add_rule_output(bots, bot, low_dest, 'min')
                    self.add_rule_bot(bots, bot, high_dest, 'max')
                elif instruction.index('output') > instruction.index('bot', 1):
                    bot, low_dest, high_dest = map(int, re.findall('\w*\d', instruction))
                    self.add_rule_bot(bots, bot, low_dest, 'min')
                    self.add_rule_output(bots, bot, high_dest, 'max')

    def give_to_bot(self, bots, bot, bins, value):
        print('bot {} receive {}'.format(bot, value))
        bots[bot]['chips'].append(value)
        if len(bots[bot]['chips']) == 2:
            min_chip = min(bots[bot]['chips'])
            max_chip = max(bots[bot]['chips'])
            if self.highlight == (min_chip, max_chip):
                self.highlight_bot = bot
            if bots[bot]['min']['type'] == 'bot':
                self.give_to_bot(bots, bots[bot]['min']['destination'], bins, min_chip)
            elif bots[bot]['min']['type'] == 'output':
                self.give_to_bin(bots, bot, bins, min_chip, 'min')
            if bots[bot]['max']['type'] == 'bot':
                self.give_to_bot(bots, bots[bot]['max']['destination'], bins, max_chip)
            elif bots[bot]['max']['type'] == 'output':
                self.give_to_bin(bots, bot, bins, max_chip, 'max')

    @staticmethod
    def give_to_bin(bots, bot, bins, chip, value):
        print('bin {} receive {}'.format(bots[bot][value]['destination'], chip))
        bins[bots[bot][value]['destination']] = chip

    @staticmethod
    def add_rule_output(bots, bot, bin_destination, value):
        if bot not in bots:
            bots[bot] = {'min': {}, 'max': {}, 'chips': []}
        bots[bot][value] = {'type': 'output', 'destination': bin_destination}
        print('bot {} give {} to output {}'.format(bot, value, bin_destination))

    @staticmethod
    def add_rule_bot(bots, bot, bot_destination, value):
        if bot not in bots:
            bots[bot] = {'min': {}, 'max': {}, 'chips': []}
        bots[bot][value] = {'type': 'bot', 'destination': bot_destination}
        print('bot {} give {} to bot {}'.format(bot, value, bot_destination))
