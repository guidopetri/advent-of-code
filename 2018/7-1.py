#! /usr/bin/env python

import re


class Step():
    def __init__(self, name, requirement):
        self.name = name
        self.reqs = [requirement]

    def add_req(self, req):
        self.reqs.append(req)

    def __repr__(self):
        temp = self.reqs
        temp.sort()
        return '; '.join(temp)


# this is a Directed Acyclic Graph problem

with open('7-input.txt', 'r') as f:
    content = f.read().split('\n')

reqs_tuples = []

for line in content:
    match = re.search(r'Step (.) must be finished before step (.) can begin.',
                      line)
    reqs_tuples.append((match.group(1), match.group(2)))

all_letters = set()
steps = {}

for tup in reqs_tuples:
    all_letters.update(tup)
    if tup[1] not in steps:
        steps[tup[1]] = Step(tup[1], tup[0])
    else:
        steps[tup[1]].add_req(tup[0])

correct_order = []

while len(correct_order) < len(all_letters):
    potentials = []
    for letter in all_letters:
        if letter in steps and hasattr(steps[letter], 'reqs'):
            if all(((x in correct_order) for x in steps[letter].reqs)):
                potentials.append(letter)
        elif letter not in steps:
            potentials.append(letter)
    potentials.sort()
    correct_order.append([x for x in potentials if x not in correct_order][0])

print(''.join(correct_order))
