#! /usr/bin/env python

from enum import Enum, unique
import re


@unique
class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Cart():

    id_counter = 0

    def __init__(self, x, y, direction):
        self.id = Cart.id_counter
        Cart.id_counter += 1
        self.x = x
        self.y = y
        self.direction = self.get_direction(direction)
        self.intersection_counter = 0

    def get_direction(self, direction):
        if direction == '^':
            return Directions.UP
        elif direction == 'v':
            return Directions.DOWN
        elif direction == '>':
            return Directions.RIGHT
        elif direction == '<':
            return Directions.LEFT
        else:
            raise ValueError('Unable to read direction at position '
                             '%s, %s' % self.x, self.y)

    def set_direction(self, direction):
        self.direction = direction

    @property
    def position(self):
        return (self.x, self.y)

    def move_forward(self):
        if self.direction == Directions.UP:
            self.y -= 1
        elif self.direction == Directions.DOWN:
            self.y += 1
        elif self.direction == Directions.LEFT:
            self.x -= 1
        elif self.direction == Directions.RIGHT:
            self.x += 1

    def turn_at_intersection(self):
        if self.intersection_counter == 0:
            self.direction = Directions((self.direction.value - 1 + 4) % 4)
        elif self.intersection_counter == 1:
            pass  # direction remains the same
        elif self.intersection_counter == 2:
            self.direction = Directions((self.direction.value + 1 + 4) % 4)
        self.intersection_counter += 1
        self.intersection_counter %= 3

    def __repr__(self):
        return 'Cart {}: {}, {}'.format(self.id,
                                        self.position,
                                        self.direction.name)


def advance_one_tick(grid, carts):
    def sorting_fn(cart):
        return cart.x + 100 * cart.y

    carts.sort(key=sorting_fn)
    cart_positions = set([cart.position for cart in carts])
    for cart in carts:
        cart_positions.remove(cart.position)
        cart.move_forward()
        if cart.position not in cart_positions:
            cart_positions.add(cart.position)
        else:
            raise ValueError('CRASH! at {}'.format(cart.position))
    for cart in carts:
        current_position = grid[cart.y][cart.x]
        if current_position == '\\':
            if cart.direction == Directions.UP:
                cart.set_direction(Directions.LEFT)
            elif cart.direction == Directions.RIGHT:
                cart.set_direction(Directions.DOWN)
            elif cart.direction == Directions.DOWN:
                cart.set_direction(Directions.RIGHT)
            elif cart.direction == Directions.LEFT:
                cart.set_direction(Directions.UP)
        elif current_position == '/':
            if cart.direction == Directions.UP:
                cart.set_direction(Directions.RIGHT)
            elif cart.direction == Directions.RIGHT:
                cart.set_direction(Directions.UP)
            elif cart.direction == Directions.DOWN:
                cart.set_direction(Directions.LEFT)
            elif cart.direction == Directions.LEFT:
                cart.set_direction(Directions.DOWN)
        elif current_position == '+':
            cart.turn_at_intersection()


def read_positions(grid):
    lines = grid.split('\n')

    carts = []

    for y in range(0, len(lines)):
        for x in range(0, len(lines[y])):
            if lines[y][x] in ('^', 'v', '>', '<'):
                carts.append(Cart(x, y, lines[y][x]))

    return carts


def join_grid(grid):
    return '\n'.join([''.join(x) for x in grid])


def place_carts(grid, carts):
    from copy import deepcopy

    replaced_grid = deepcopy(grid)

    # pretty-print colors
    RED = '\033[0;31m'
    NC = '\033[0m'  # No Color

    for cart in carts:
        if cart.direction == Directions.UP:
            character = '^'
        elif cart.direction == Directions.DOWN:
            character = 'v'
        elif cart.direction == Directions.LEFT:
            character = '<'
        elif cart.direction == Directions.RIGHT:
            character = '>'

        character = RED + character + NC

        replaced_grid[cart.y][cart.x] = character

    return replaced_grid


with open('13-input.txt', 'r') as f:
    content = f.read()

example_content = """/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   """  # noqa

carts = read_positions(content)
cartless_grid = re.sub(r'>|<', '-', content)
cartless_grid = re.sub(r'\^|v', '|', cartless_grid)
grid = [list(x) for x in cartless_grid.split('\n')]

for i in range(1000):
    try:
        advance_one_tick(grid, carts)
    except ValueError as e:
        new_grid = place_carts(grid, carts)
        print(join_grid(new_grid))
        raise e
