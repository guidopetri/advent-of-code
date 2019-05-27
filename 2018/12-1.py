#! /usr/bin/env python

import re


def next_gen(last_gen, rules):
    new_gen = []
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
        # regex = r'(?<=' + rule[:2] + r')(' + rule[2:3] + r')
        # (?=' + rule[3:] + r')'

    return ''.join(new_gen)


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

plant_sum = 0
last_gen = initial_state
plant_sum += last_gen.count('#')
for generation in range(20):
    print('{}: '.format(generation), plant_sum, last_gen)
    new_state = next_gen(last_gen, rules)
    # print('new gen')
    plant_sum += new_state.count('#')
    last_gen = new_state
