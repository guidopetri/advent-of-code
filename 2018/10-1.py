#! /usr/bin/env python

import re


class Point():

    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def move_ahead(self):
        self.position = (sum(x) for x in zip(self.position, self.velocity))

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

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

for line in example_content:
    points.append(find_point(line))

print(points)
