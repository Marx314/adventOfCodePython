from copy import copy
from src.AStarSearch import AStarSearch
from src.AStarSearch import AStarSearchGraph

BOSS_HP_DECREASE = 'bhp'
YOUR_HP_INCREASE = 'yhp'


class Search(AStarSearch):
    def heuristic(self, goal, current, next):
        return 0

    def search_until(self, current, goal):
        boss, you, spell_stack, action = current
        if self.is_first_move(you):
            return False
        spell_stack.apply_spell(you, boss)
        if self.is_dead(boss):
            return True
        you.hp -= max(boss.damage - you.armor, 1)
        if self.is_dead(you):
            return False
        spell_stack.apply_spell(you, boss)
        if self.is_dead(boss):
            return True
        return False

    @staticmethod
    def is_first_move(you):
        return you.mana_spent == 0

    @staticmethod
    def is_dead(p):
        return p.hp <= 0


class Game(AStarSearchGraph):
    def cost(self, current, next):
        return next[1].mana_spent - current[1].mana_spent

    @staticmethod
    def generate_node(spell, boss, you, spell_stack, actions):
        b, y, s = boss.copy(), you.copy(), spell_stack.copy()
        y.mana -= spell[1]['cost']
        y.mana_spent += spell[1]['cost']
        if BOSS_HP_DECREASE in spell[1]:
            b.hp -= spell[1][BOSS_HP_DECREASE]
        if YOUR_HP_INCREASE in spell[1]:
            y.hp += spell[1][YOUR_HP_INCREASE]
        if spell[0] in ('Shield', 'Poison', 'Recharge'):
            s.add(spell[0], spell[1]['duration'])
        actions += ('You casted {} - {} - {} - {}'.format(spell[0], y, b, s),)
        return b, y, s, actions

    def neighbors(self, current):
        boss, you, spell_stack, actions = current
        possibilities = []
        spells = {
            'Magic Missile': {'cost': 53, BOSS_HP_DECREASE: 4},
            'Drains': {'cost': 73, BOSS_HP_DECREASE: 2, YOUR_HP_INCREASE: 2},
            'Shield': {'cost': 113, 'duration': 6},
            'Poison': {'cost': 173, 'duration': 6},
            'Recharge': {'cost': 229, 'duration': 5},
        }

        if you.hp <= 0:
            return []
        active_spell = [spell_name for spell_name, _ in spell_stack.spells]
        for spell in spells.items():
            if you.mana >= spell[1]['cost'] and spell[0] not in active_spell:
                possibilities.append(self.generate_node(spell, boss, you, spell_stack, actions))

        return possibilities


class GameLosingOnePointEachPlayerTurn(Game):
    def neighbors(self, current):
        boss, you, spell_stack, action = current
        you.hp -= 1
        return super(GameLosingOnePointEachPlayerTurn, self).neighbors(current)


class SpellStack(object):
    spells = []

    def __init__(self, spells=[]):
        self.spells = spells

    def add(self, spell, state):
        self.spells.append((spell, state))

    def apply_spell(self, you, boss):
        new_spell_state = []
        for i in range(len(self.spells)):
            spell, state = self.spells[i]
            if spell == 'Shield':
                if state == 6:
                    you.armor += 7
                elif state == 1:
                    you.armor -= 7
            if spell == 'Poison':
                boss.hp -= 3
            if spell == 'Recharge':
                you.mana += 101
            state -= 1
            if state != 0:
                new_spell_state.append((spell, state))
        self.spells = new_spell_state

    def copy(self):
        return SpellStack(copy(self.spells))

    def __str__(self):
        return 'SS({})'.format(self.spells)


class Boss(object):
    hp = 0
    damage = 0

    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def copy(self):
        return Boss(self.hp, self.damage)

    def __lt__(self, other):
        return self.hp < other.hp

    def __str__(self):
        return 'Boss({})'.format(self.hp)


class You(object):
    hp = 0
    mana = 0
    armor = 0
    mana_spent = 0

    def __init__(self, hp, mana, armor=0, mana_spent=0):
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.mana_spent = mana_spent

    def copy(self):
        return You(self.hp, self.mana, self.armor, self.mana_spent)

    def __str__(self):
        return 'You({}, {}, {})'.format(self.hp, self.mana, self.armor)


class Day22(object):
    @staticmethod
    def find_best_fight_config(you, boss):
        graph = Game()
        start = (boss, you, SpellStack(), tuple())
        came_from, cost_so_far, current = Search().a_star_search(graph, start, '')
        return cost_so_far[current]

    @staticmethod
    def find_best_fight_config_hard(you, boss):
        graph = GameLosingOnePointEachPlayerTurn()
        start = (boss, you, SpellStack(), tuple())
        came_from, cost_so_far, current = Search().a_star_search(graph, start, '')
        return cost_so_far[current]
