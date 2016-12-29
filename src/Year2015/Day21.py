import itertools
import math


def lose_against_boss(you, boss):
    return not win_against_boss(you, boss)


def win_against_boss(you, boss):
    boss_damage = max(you.damage - boss['armor'], 1)
    you_damage = max(boss['damage'] - you.armor, 1)
    turn_to_kill_boss = math.ceil(boss['hp'] / boss_damage)
    turn_to_kill_you = math.ceil(you.hp / you_damage)
    return turn_to_kill_boss <= turn_to_kill_you


class Build(object):
    cost = 0
    weapon_name = None
    armor_name = None
    damage = 0
    rings = []

    def __init__(self, you, cost=0, weapon=None, armor=None, rings=None):
        self.hp = you['hp']
        self.damage = you['damage']
        self.armor = you['armor']
        self.cost = cost
        self.weapon_name = weapon
        self.armor_name = armor
        self.rings = [] if rings is None else rings

    def add_weapon(self, name, store):
        self.weapon_name = name
        self.cost += store['Weapons'][name]['Cost']
        self.damage += store['Weapons'][name]['Damage']

    def add_armor(self, name, store):
        self.armor_name = name
        self.cost += store['Armors'][name]['Cost']
        self.armor += store['Armors'][name]['Armor']

    def add_ring(self, name, store):
        self.rings.append(name)
        self.cost += store['Rings'][name]['Cost']
        self.armor += store['Rings'][name]['Armor']
        self.damage += store['Rings'][name]['Damage']

    def copy(self):
        return Build({'hp': self.hp, 'damage': self.damage, 'armor': self.armor}, self.cost, self.weapon_name,
                     self.armor_name, self.rings)


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
            'Armors': {
                'Leather': {'Cost': 13, 'Armor': 1},
                'Chainmail': {'Cost': 31, 'Armor': 2},
                'Splintmail': {'Cost': 53, 'Armor': 3},
                'Bandedmail': {'Cost': 75, 'Armor': 4},
                'Platemail': {'Cost': 102, 'Armor': 5},
            },
            'Rings': {
                'Damage +1': {'Cost': 25, 'Armor': 0, 'Damage': 1},
                'Damage +2': {'Cost': 50, 'Armor': 0, 'Damage': 2},
                'Damage +3': {'Cost': 100, 'Armor': 0, 'Damage': 3},
                'Defense +1': {'Cost': 20, 'Armor': 1, 'Damage': 0},
                'Defense +2': {'Cost': 40, 'Armor': 2, 'Damage': 0},
                'Defense +3': {'Cost': 60, 'Armor': 3, 'Damage': 0},
            },
        }

    def iterate_build(self, you, boss, outcome=win_against_boss):
        possibilities = []
        build_you = Build(you)
        possibilities.extend(self.just_weapons(boss, outcome, build_you))
        possibilities.extend(self.armor_with_weapon(boss, outcome, build_you))
        possibilities.extend(self.ring_and_weapon(boss, outcome, build_you, 1))
        possibilities.extend(self.ring_and_weapon(boss, outcome, build_you, 2))
        possibilities.extend(self.ring_armor_and_weapon(boss, outcome, build_you, 1))
        possibilities.extend(self.ring_armor_and_weapon(boss, outcome, build_you, 2))
        possibilities = sorted(possibilities, key=lambda x: x.cost)

        return possibilities

    def ring_armor_and_weapon(self, boss, outcome, you, ring_count):
        possibilities = []
        for rings in itertools.combinations(self.store['Rings'].keys(), ring_count):
            copy_of_you = you.copy()
            for i in range(ring_count):
                copy_of_you.add_ring(rings[i], self.store)

            possibilities.extend(self.armor_with_weapon(boss, outcome, copy_of_you))

        return possibilities

    def ring_and_weapon(self, boss, outcome, you, ring_count):
        possibilities = []
        for rings in itertools.combinations(self.store['Rings'].keys(), ring_count):
            copy_of_you = you.copy()
            for i in range(ring_count):
                copy_of_you.add_ring(rings[i], self.store)

            possibilities.extend(self.just_weapons(boss, outcome, copy_of_you))

        return possibilities

    def armor_with_weapon(self, boss, outcome, you):
        possibilities = []
        for armor in self.store['Armors'].keys():
            copy_of_you = you.copy()
            copy_of_you.add_armor(armor, self.store)

            possibilities.extend(self.just_weapons(boss, outcome, copy_of_you))

        return possibilities

    def just_weapons(self, boss, outcome, you):
        possibilities = []
        for weapon in self.store['Weapons'].keys():
            copy_of_you = you.copy()
            copy_of_you.add_weapon(weapon, self.store)
            if outcome(copy_of_you, boss):
                possibilities.append(copy_of_you)

        return possibilities
