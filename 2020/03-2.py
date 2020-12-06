#! /usr/bin/env python3

from functools import reduce
from operator import mul


def get_number_of_trees(slope):
    down_by, right_by = slope
    horz_len = len(data[0])

    current_idx = (0, 0)

    at_bottom = lambda: current_idx[0] + 1 == len(data)
    trees = 0

    while True:
        current_idx = (current_idx[0] + down_by,
                       (current_idx[1] + right_by) % horz_len)

        trees += data[current_idx[0]][current_idx[1]] == '#'
        if at_bottom():
            break
    return trees


with open('03-input.txt', 'r') as f:
    data = f.readlines()

data = [list(x.strip()) for x in data]

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

tree_counts = map(get_number_of_trees, slopes)

result = reduce(mul, tree_counts)

print(result)
