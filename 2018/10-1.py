#! /usr/bin/env python

import re
from collections import OrderedDict


class Point():

    def __init__(self, position, velocity):
        self.position = position
        self.velo = velocity

    def move_ahead(self):
        self.position = tuple(sum(x) for x in zip(self.position, self.velo))

    def move_behind(self):
        neg_velo = (-x for x in self.velo)
        self.position = tuple(sum(x) for x in zip(self.position, neg_velo))

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velo

    def __repr__(self):
        pos = self.get_position()
        vel = self.get_velocity()
        return "Point at {} with velocity {}".format(pos, vel)


def find_point(line):
    match = re.search(r'(?<=position=<)([\s0-9\-]+),([\s0-9\-]+)>'
                      r' velocity=<([\s0-9\-]+),([\s0-9\-]+)>', line)
    position = (int(match.group(1)), int(match.group(2)))
    velocity = (int(match.group(3)), int(match.group(4)))
    new_point = Point(position, velocity)
    return new_point


def get_furthest_positions(points):
    max_x = 0
    max_y = 0

    min_x = 0
    min_y = 0

    positions = [point.get_position() for point in points]

    max_x = max(positions, key=lambda x: x[0])[0]
    max_y = max(positions, key=lambda x: x[1])[1]

    min_x = min(positions, key=lambda x: x[0])[0]
    min_y = min(positions, key=lambda x: x[1])[1]
    return max_x, max_y, min_x, min_y


def compose_image(points):
    max_x, max_y, min_x, min_y = get_furthest_positions(points)

    lines = OrderedDict()
    for y in range(min_y, max_y + 1):
        lines[y] = OrderedDict()
        for x in range(min_x, max_x + 1):
            cell = '.'
            lines[y][x] = cell

    for point in points:
        pos = point.get_position()

        lines[pos[1]][pos[0]] = '#'

    newlines = [''.join(line.values()) for line in lines.values()]
    image = '\n'.join(newlines)

    return image


def calculate_distance(points):
    max_x, max_y, min_x, min_y = get_furthest_positions(points)

    distance_x = abs(max_x - min_x)
    distance_y = abs(max_y - min_y)

    return distance_x + distance_y


with open('10-input.txt', 'r') as f:
    content = f.read().split('\n')

example_content = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>""".split('\n')

points = []

for line in content:
    points.append(find_point(line))

loopcount = 0
distance = calculate_distance(points)
last_distance = distance + 1
while distance < last_distance:
    if loopcount % 1000 == 0:
        print("looped {} times. distance is {}".format(loopcount, distance))
    if loopcount > 200000:
        print("early break")
        break
    loopcount += 1
    [point.move_ahead() for point in points]
    last_distance = distance
    distance = calculate_distance(points)

loopcount -= 1
[point.move_behind() for point in points]

print("Took {} seconds. Smallest distance is {}".format(loopcount, distance))

ascii_image = compose_image(points)
print(ascii_image)
