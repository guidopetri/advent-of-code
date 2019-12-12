#! /usr/bin/env python3

from collections import deque


class Planet(object):

    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def set_parent(self, parent):
        self.parent = parent
        parent.set_child(self)

    def set_child(self, child):
        self.children.append(child)


with open('06-input.txt', 'r') as f:
    orbits = f.readlines()

orbits = [orbit.strip().split(')') for orbit in orbits]

planets = {}

for parent, child in orbits:
    planets[parent] = Planet(parent)
    planets[child] = Planet(child)

for parent, child in orbits:
    planets[child].set_parent(planets[parent])

start_node = planets['YOU'].parent
end_node = planets['SAN'].parent

planet_walker = deque([(0, start_node)])
planets_visited = set()

while len(planet_walker) > 0:
    step, planet = planet_walker.popleft()
    planets_visited.add(planet)
    if planet == end_node:
        print('Took {} steps'.format(step))
        break
    if planet.parent is not None:
        planet_walker.append((step + 1, planet.parent))
    if planet.children:
        for child in planet.children:
            if child not in planets_visited:
                planet_walker.append((step + 1, child))
