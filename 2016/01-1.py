#! /usr/bin/env python

from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


with open('01-input.txt', 'r') as f:
    data = f.read().split(', ')

current_direction = Direction.NORTH
loc = [0, 0]

for instruction in data:
    if instruction[0] == 'R':
        current_direction = Direction((current_direction.value + 1) % 4)
    elif instruction[0] == 'L':
        current_direction = Direction((current_direction.value + 3) % 4)

    block_count = int(instruction[1:])
    add_subtract = 1 if current_direction.value in (0, 1) else -1

    loc[current_direction.value % 2] += (block_count * add_subtract)

print('Bunny location: {}'.format(loc))

distance = abs(loc[0]) + abs(loc[1])

print('Distance: {}'.format(distance))
