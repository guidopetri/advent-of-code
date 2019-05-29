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
    by_id = {}

    def __init__(self, x, y, direction):
        self.id = Cart.id_counter
        Cart.id_counter += 1
        Cart.by_id[self.id] = self
        self.x = x
        self.y = y
        self.direction = self.get_direction(direction)
        self.intersection_counter = 0
        self.alive = True

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

    def crash(self):
        print("cart {} crashed at {}".format(self.id, self.position))
        self.alive = False

    def __repr__(self):
        return 'Cart {}: {}, {}'.format(self.id,
                                        self.position,
                                        self.direction.name)


def advance_one_tick(grid, carts):
    def sorting_fn(cart):
        return cart.x + 100 * cart.y

    carts.sort(key=sorting_fn)
    intact_carts = [cart for cart in carts if cart.alive]
    cart_positions = {cart.id: cart.position for cart in intact_carts}
    for cart in intact_carts:
        cart.move_forward()
        if cart.position not in cart_positions.values():
            cart_positions[cart.id] = cart.position
        else:
            for cart_id, position in cart_positions.items():
                if position == cart.position and Cart.by_id[cart_id].alive:
                    Cart.by_id[cart_id].crash()
            cart.crash()
    for cart in intact_carts:
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
    GRN = '\033[0;32m'
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

        character = RED * (not cart.alive) + GRN * cart.alive + character + NC

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

second_example = """/>-<\\  
|   |  
| /<+-\\
| | | v
\\>+</ |
  |   ^
  \\<->/"""  # noqa

carts = read_positions(content)
cartless_grid = re.sub(r'>|<', '-', content)
cartless_grid = re.sub(r'\^|v', '|', cartless_grid)
grid = [list(x) for x in cartless_grid.split('\n')]

while len([cart for cart in carts if cart.alive]) > 1:
    advance_one_tick(grid, carts)

new_grid = place_carts(grid, carts)
print(join_grid(new_grid))
print([cart for cart in carts if cart.alive])
