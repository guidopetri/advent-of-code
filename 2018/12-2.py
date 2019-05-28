#! /usr/bin/env python

import re


def next_gen(last_gen, rules):
    new_gen = []
    last_gen = last_gen
    for index_pot in range(0, len(last_gen)):
        if index_pot < 1:
            rule = '..' + last_gen[index_pot:index_pot + 3]
        elif index_pot < 2:
            rule = '.' + last_gen[index_pot - 1:index_pot + 3]
        elif len(last_gen) - index_pot < 2:
            rule = last_gen[index_pot - 2:index_pot + 1] + '..'
        elif len(last_gen) - index_pot < 3:
            rule = last_gen[index_pot - 2:index_pot + 2] + '.'
        else:
            rule = last_gen[index_pot - 2:index_pot + 3]

        rule = ''.join(rule)

        if rule in rules:
            result = rules[rule]
        else:
            result = '.'

        new_gen.append(result)
    new_gen = ''.join(new_gen)
    return new_gen


generation_count = 127

# read input
with open('12-input.txt', 'r') as f:
    content = f.read()

initial_state = re.search(r'initial state: ([\.\#]+?)\n',
                          content).group(1)

rules = {}
for match in re.finditer(r'([\.\#]{5}) => ([\.\#])', content):
    rules[match.group(1)] = match.group(2)

# i now realize that the indices of the pots matter, because we need to
# add them up.
surrounding_pots = ''.join(['.' for x in range(generation_count)])
last_gen = surrounding_pots[:5] + initial_state + surrounding_pots

for generation in range(generation_count):
    print('{}: '.format(generation), last_gen)
    new_state = next_gen(last_gen, rules)
    last_gen = new_state

plant_sum = 0

for index in range(0, len(last_gen)):
    if last_gen[index] == '#':
        plant_sum = plant_sum + index - 5

# print('{}: '.format(generation_count), last_gen)
print('\nSum of plant-containing pot indices: {}'.format(plant_sum))

# it seems after ~generation 127, the structure becomes regular and every
# generation moves the plants one pot forward. this translates to every
# generation adding 36 to the plant-containing pot indices sum.

# ergo: 50 billion minus 127, times 36, plus the value at 127:

# value at 127
4030

# 50b minus 127
5e10 - 127

# result
print((5e10 - 127) * 36 + 4030)
