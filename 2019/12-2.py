#! /usr/bin/env python3

from itertools import combinations


class Planet(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def apply_velocity(self):
        self.x += self.x_vel
        # self.y += self.y_vel
        # self.z += self.z_vel

    @property
    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    @property
    def kinetic_energy(self):
        return abs(self.x_vel) + abs(self.y_vel) + abs(self.z_vel)

    @property
    def total_energy(self):
        return self.potential_energy * self.kinetic_energy

    def __repr__(self):
        return 'Planet(pos=<x={}, y={}, z={}>, ' \
               'vel=<x={}, y={}, z={}>)'.format(self.x,
                                                self.y,
                                                self.z,
                                                self.x_vel,
                                                self.y_vel,
                                                self.z_vel,
                                                )

    def describe(self):
        return (self.x, self.y, self.z, self.x_vel, self.y_vel, self.z_vel)

    def x_stopped(self):
        return self.x_vel == 0


with open('12-input.txt', 'r') as f:
    initial_positions = f.readlines()

# sample input
# initial_positions = """<x=-1, y=0, z=2>
#                        <x=2, y=-10, z=-7>
#                        <x=4, y=-8, z=8>
#                        <x=3, y=5, z=-1>""".split('\n')
# initial_positions = """<x=-8, y=-10, z=0>
#                        <x=5, y=5, z=10>
#                        <x=2, y=-7, z=3>
#                        <x=9, y=-8, z=-3>""".split('\n')

planets = []

for pos in initial_positions:
    pos = pos.split('<')[1].split('>')[0]
    pos = pos.split(', ')
    x = pos[0]
    y = pos[1]
    z = pos[2]
    planet = Planet(int(x.split('=')[1]),
                    int(y.split('=')[1]),
                    int(z.split('=')[1]),
                    )
    planets.append(planet)

previous_states = set()
n_iter = 0

while True and n_iter < 10000000000:
    if all([planet.x_stopped() for planet in planets]):
        state = tuple([planet.describe() for planet in planets])
        if state in previous_states:
            break
        previous_states.add(state)

    for permutation in combinations(planets, 2):
        first = permutation[0]
        second = permutation[1]

        first.x_vel -= int(first.x > second.x)
        second.x_vel += int(first.x > second.x)
        first.x_vel += int(first.x < second.x)
        second.x_vel -= int(first.x < second.x)

        # first.y_vel -= int(first.y > second.y)
        # second.y_vel += int(first.y > second.y)
        # first.y_vel += int(first.y < second.y)
        # second.y_vel -= int(first.y < second.y)

        # first.z_vel -= int(first.z > second.z)
        # second.z_vel += int(first.z > second.z)
        # first.z_vel += int(first.z < second.z)
        # second.z_vel -= int(first.z < second.z)

    for planet in planets:
        planet.apply_velocity()

    n_iter += 1

    if n_iter % 100000 == 0:
        print(n_iter)

print(n_iter)
