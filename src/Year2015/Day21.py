class Day21(object):
    def __init__(self):
        self.store = {
            'Weapons': {
                'Dagger': {'Cost': 8, 'Damage': 4},
                'Shortsword': {'Cost': 10, 'Damage': 5},
                'Warhammer': {'Cost': 25, 'Damage': 6},
                'Longsword': {'Cost': 40, 'Damage': 7},
                'Greataxe': {'Cost': 74, 'Damage': 8}
            },
            'Armor': {
                'Leather': {'Cost': 13, 'Armor': 1},
                'Chainmail': {'Cost': 31, 'Armor': 2},
                'Splintmail': {'Cost': 53, 'Armor': 3},
                'Bandedmail': {'Cost': 75, 'Armor': 4},
                'Platemail': {'Cost': 102, 'Armor': 5},
            },
            'Rings': {
                'Damage +1': {'Cost': 25, 'Armor': 0, 'Damage': 1},
                'Damage +2': {'Cost': 50, 'Armor': 0, 'Damage': 1},
                'Damage +3': {'Cost': 100, 'Armor': 0, 'Damage': 1},
                'Defense +1': {'Cost': 20, 'Armor': 1, 'Damage': 0},
                'Defense +2': {'Cost': 40, 'Armor': 1, 'Damage': 0},
                'Defense +3': {'Cost': 60, 'Armor': 1, 'Damage': 0},
            },
        }

    def doyousurviveagainstboss(self, you, boss):
        boss_damage = max(you['damage'] - boss['armor'], 1)
        you_damage = max(boss['damage'] - you['armor'], 1)
        turn_to_kill_boss = boss['hp'] / boss_damage
        turn_to_kill_you = you['hp'] / you_damage
        return turn_to_kill_boss <= turn_to_kill_you

    def minimal_cost(self):
        return min([weapon['Cost'] for weapon in self.store['Weapons'].itervalues() if weapon['Cost'] < min])
