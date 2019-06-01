#! /usr/bin/env python

import re
from collections import deque


class Position(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        attrs = []
        for value in self.__dict__:
            attrs.append(value + ' = ' + str(getattr(self, value)))
        return '(' + ', '.join((attrs)) + ')'

    def __eq__(self, other):
        if type(other) == type(self):
            return other.__dict__ == self.__dict__
        else:
            return False

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class BattleMap(object):

    def __init__(self, data):
        self.data = data.split('\n')

    def get_position(self, position):
        return self.data[position.y][position.x]

    def __repr__(self):
        return '\n'.join(self.data)


class BattleUnit(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.atk = 3
        self.hp = 200
        self.alive = True
        self.add_to_counter(self)

    @classmethod
    def add_to_counter(cls, self):
        cls.units.append(self)

    @classmethod
    def remove_from_counter(cls, self):
        cls.units.remove(self)

    @property
    def position(self):
        return Position(self.x, self.y)

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

            attackable = [x for x in attackable if x.hp == attackable[0].hp]
            find_order(attackable)
            other = attackable[0]
            other.hp -= self.atk
            if other.hp < 1:
                other.alive = False
                other.remove_from_counter(other)

    def move(self, units, full_map):
        for unit in units:
            if self != unit:
                distance = find_shortest_path(self.position,
                                              unit.position,
                                              full_map)
                print(units[0], distance)
                break
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
    burned = set()
    while len(queue):
        loc, distance = queue.popleft()
        distance += 1
        neighboring_pos = [Position(loc.x + 1, loc.y),
                           Position(loc.x - 1, loc.y),
                           Position(loc.x, loc.y + 1),
                           Position(loc.x, loc.y - 1)]
        new_positions = [pos for pos in neighboring_pos if pos not in burned]
        for position in new_positions:
            burned.add(position)
            if position == pos2:
                return distance
            if full_map.get_position(position) == '#':
                continue
            elif full_map.get_position(position) == '.':
                queue.append((position, distance))
    return None


with open('15-input.txt', 'r') as f:
    raw_data = f.read()

map_raw = re.sub(r'G|E', '.', raw_data)
map_parsed = BattleMap(raw_data)

y = 0
for line in raw_data.split('\n'):
    for match in re.finditer(r'(G|E)', line):
        if match[1] == 'G':
            unit_type = Goblin
        elif match[1] == 'E':
            unit_type = Elf
        x = match.start(1)
        new_unit = unit_type(x, y)
    y += 1

round_counter = 0

print(Goblin.units[0].position,
      Elf.units[0].position, flush=True)
distance = find_shortest_path(Goblin.units[0].position,
                              Elf.units[0].position,
                              map_parsed)
print(distance, flush=True)

while Goblin.units and Elf.units:
    units = Goblin.units + Elf.units
    find_order(units)
    for unit in units:
        unit.move(units, map_parsed)
        unit.attack(units)
    round_counter += 1
    break

rounds_completed = round_counter - 1
units_remaining = Goblin.units + Elf.units
hp_sum = sum([unit.hp for unit in units_remaining])

print(rounds_completed * hp_sum)
