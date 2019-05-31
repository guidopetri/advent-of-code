#! /usr/bin/env python

from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


with open('01-input.txt', 'r') as f:
    data = f.read().split(', ')
    example_data = "R8, R4, R4, R8".split(', ')

current_direction = Direction.NORTH
loc = [0, 0]
visited_locations = set()

for instruction in data:
    if instruction[0] == 'R':
        current_direction = Direction((current_direction.value + 1) % 4)
    elif instruction[0] == 'L':
        current_direction = Direction((current_direction.value + 3) % 4)

    block_count = int(instruction[1:])
    add_subtract = 1 if current_direction.value in (0, 1) else -1

    visited = False
    for i in range(block_count):
        loc[current_direction.value % 2] += (1 * add_subtract)
        if tuple(loc) not in visited_locations:
            visited_locations.add(tuple(loc))
        else:
            visited = True
            break
    if visited:
        break


print('Bunny location: {}'.format(loc))

distance = abs(loc[0]) + abs(loc[1])

print('Distance: {}'.format(distance))
