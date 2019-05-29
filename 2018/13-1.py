#! /usr/bin/env python

from enum import Enum, unique


@unique
class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Cart():

    def __init__(self, x, y, direction):
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
        return 'Cart: {}, {}'.format(self.position, self.direction.name)


def advance_one_tick(grid, carts):
    cart_positions = set()
    for cart in carts:
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


with open('13-input.txt', 'r') as f:
    content = f.read()

example_content = """/->-\\        
|   |  /----\\
| /-+--+-\\  |
| | |  | v  |
\\-+-/  \\-+--/
  \\------/   """  # noqa

carts = read_positions(example_content)
grid = [list(x) for x in example_content.split('\n')]

print(carts)

for i in range(15):
    advance_one_tick(grid, carts)
    # if i > 600:
    #     print(carts)
