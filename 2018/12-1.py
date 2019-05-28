#! /usr/bin/env python

import re


def next_gen(last_gen, rules):
    new_gen = []
    last_gen = '....' + last_gen + '....'
    for index_pot in range(4, len(last_gen) - 1):
        rule = last_gen[index_pot - 3:index_pot + 2]
        rule = ''.join(rule)

        if rule in rules:
            result = rules[rule]
        else:
            result = '.'

        new_gen.append(result)
        # regex = r'(?<=' + rule[:2] + r')(' + rule[2:3] + r')
        # (?=' + rule[3:] + r')'
    new_gen = ''.join(new_gen)
    new_gen = new_gen.strip('.')
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
                          example_content).group(1)

rules = {}
for match in re.finditer(r'([\.\#]{5}) => ([\.\#])', example_content):
    rules[match.group(1)] = match.group(2)

# i now realize that the indices of the pots matter, because we need to
# add them up.

plant_sum = 0
last_gen = initial_state
plant_sum += last_gen.count('#')
for generation in range(20):
    print('{}: '.format(generation), plant_sum, last_gen)
    new_state = next_gen(last_gen, rules)
    # print('new gen')
    plant_sum += new_state.count('#')
    last_gen = new_state
