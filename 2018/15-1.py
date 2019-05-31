#! /usr/bin/env python

import re


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

    @property
    def position(self):
        pos = Position()
        pos.x = self.x
        pos.y = self.y
        return pos

    @property
    def team(self):
        pass  # default implementation

    def __repr__(self):
        return "{} unit: {}".format(self.team, self.position)


class Goblin(BattleUnit):

    @property
    def team(self):
        return "Goblin"


class Elf(BattleUnit):

    @property
    def team(self):
        return "Elf"


def find_order(units):
    def read_order_priority(unit):
        priority = unit.position.x + 100 * unit.position.y
        return priority

    units.sort(key=read_order_priority)
    return units


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

print(units)
