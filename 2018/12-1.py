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


# read input
with open('12-input.txt', 'r') as f:
    content = f.read()

example_content = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

initial_state = re.search(r'initial state: ([\.\#]+?)\n',
                          content).group(1)

rules = {}
for match in re.finditer(r'([\.\#]{5}) => ([\.\#])', content):
    rules[match.group(1)] = match.group(2)

# i now realize that the indices of the pots matter, because we need to
# add them up.
surrounding_pots = ''.join(['.' for x in range(20)])
last_gen = surrounding_pots + initial_state + surrounding_pots

for generation in range(20):
    print('{}: '.format(generation), last_gen)
    new_state = next_gen(last_gen, rules)
    last_gen = new_state

plant_sum = 0

for index in range(0, len(last_gen)):
    if last_gen[index] == '#':
        plant_sum = plant_sum + index - 20

print('20: ', last_gen)
print('\nSum of plant-containing pot indices: {}'.format(plant_sum))
