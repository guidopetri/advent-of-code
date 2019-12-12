#! /usr/bin/env python3

from collections import deque


class Planet(object):

    def __init__(self, name):
        self.name = name
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


with open('06-input.txt', 'r') as f:
    orbits = f.readlines()

orbits = [orbit.strip().split(')') for orbit in orbits]

planets = {}

for parent, child in orbits:
    planets[parent] = Planet(parent)
    planets[child] = Planet(child)

for parent, child in orbits:
    planets[child].set_parent(planets[parent])

orbit_count = 0

planet_walker = deque(planets.values())

while len(planet_walker) > 0:
    planet = planet_walker.popleft()
    if planet.parent is not None:
        orbit_count += 1
        planet_walker.append(planet.parent)

print(orbit_count)
