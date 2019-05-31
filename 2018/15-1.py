#! /usr/bin/env python

import re
from collections import deque


class Position(object):

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        attrs = []
        for value in self.__dict__:
            attrs.append(value + ' = ' + str(getattr(self, value)))
        return '(' + ', '.join((attrs)) + ')'


class BattleUnit(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.atk = 3
        self.hp = 200
        self.add_to_counter(self)

    @classmethod
    def add_to_counter(cls, self):
        cls.units.append(self)

    @property
    def position(self):
        pos = Position()
        pos.x = self.x
        pos.y = self.y
        return pos

    @property
    def team(cls):
        pass  # default implementation

    def attack(self, units):
        attackable = []
        for unit in units:
            if get_distance(self, unit) == 1:
                attackable.append(unit)
        if attackable:
            if len(attackable) > 1:
                attackable.sort(key=lambda x: x.hp)

            # TODO: find reading order minimum as well
            other = attackable[0]
            other.hp -= self.atk
            # TODO: check if other died and set appropriate flag / del him

    def move(self, units):
        # step 1: find range (squares adjacent to any target, not occupied)
        # step 2: if already in range, return
        # step 3: find reachable squares
        # step 4: pick nearest squares
        # step 5: choose in reading order
        # step 6: move in that direction (again in reading order)
        pass

    def __repr__(self):
        return "{} unit: {}".format(self.team, self.position)


class Goblin(BattleUnit):

    units = []

    @property
    def team(self):
        return "Goblin"


class Elf(BattleUnit):

    units = []

    @property
    def team(self):
        return "Elf"


def find_order(units):
    def read_order_priority(unit):
        priority = unit.position.x + 100 * unit.position.y
        return priority

    units.sort(key=read_order_priority)
    return


def find_nearest(unit_pos, other_pos):
    distances = {}
    for pos in other_pos:
        distances[pos] = get_distance(unit_pos, pos)

    min_distance = min(distances.values())

    return [pos for pos in other_pos if distances[pos] == min_distance]


def get_distance(pos1, pos2):
    return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)


def find_shortest_path(origin, pos2, full_map):
    queue = deque()
    queue.append((origin, 0))
    while len(queue):
        loc, distance = queue.popleft()
        if loc == pos2:
            return distance
        neighboring_positions = [(loc.x + 1, loc.y),
                                 (loc.x - 1, loc.y),
                                 (loc.x, loc.y + 1),
                                 (loc.x, loc.y - 1)]
        for position in neighboring_positions:
            if full_map.get_position(position) == '.':
                queue.append((position, distance + 1))
    return None


with open('15-input.txt', 'r') as f:
    raw_data = f.read()

battle_map = re.sub(r'G|E', '.', raw_data)

units = []

y = 0
for line in raw_data.split('\n'):
    for match in re.finditer(r'(G|E)', line):
        if match[1] == 'G':
            unit_type = Goblin
        elif match[1] == 'E':
            unit_type = Elf
        x = match.start(1)
        new_unit = unit_type(x, y)
        units.append(new_unit)
    y += 1

round_counter = 0

while Goblin.units and Elf.units:
    find_order(units)
    for unit in units:
        unit.move(units)
        unit.attack(units)
    round_counter += 1
    break

rounds_completed = round_counter - 1
units_remaining = Goblin.units + Elf.units
hp_sum = sum([unit.hp for unit in units_remaining])

print(rounds_completed * hp_sum)
# print(Elf.units)
