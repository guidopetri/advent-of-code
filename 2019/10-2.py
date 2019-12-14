#! /usr/bin/env python3

import numpy as np


def calc_angle(loc_1, loc_2):
    diff = (loc_2[0] - loc_1[0], loc_1[1] - loc_2[1])
    loc_2_norm = diff / np.linalg.norm(diff)
    result = np.arccos(np.clip(np.dot((0, 1), loc_2_norm), -1, 1))
    if diff[0] < 0:
        result = np.pi * 2 - result
    return round(result, 4)


def calc_dist(loc_1, loc_2):
    return (loc_1[0] - loc_2[0]) ** 2 + (loc_1[1] - loc_2[1]) ** 2


with open('10-input.txt', 'r') as f:
    data = f.readlines()

asteroid = (20, 19)

# sample input
# data = """.#..##.###...#######
#           ##.############..##.
#           .#.######.########.#
#           .###.#######.####.#.
#           #####.##.#.##.###.##
#           ..#####..#.#########
#           ####################
#           #.####....###.#.#.##
#           ##.#################
#           #####.##.###..####..
#           ..######..##.#######
#           ####.##.####...##..#
#           .#####..#.######.###
#           ##...#.##########...
#           #.##########.#######
#           .####.#.###.###.#.##
#           ....##.##.###..#####
#           .#.#.###########.###
#           #.#.#.#####.####.###
#           ###.##.####.##.#..##""".split('\n')
# asteroid = (11, 13)

data = [x.strip() for x in data]

asteroid_locs = [(x_idx, y_idx)
                 for y_idx, row in enumerate(data)
                 for x_idx, point in enumerate(row)
                 if point == '#']

angles = []

for other in asteroid_locs:
    if other == asteroid:
        continue
    angles.append((other,
                   calc_angle(asteroid, other),
                   calc_dist(asteroid, other))
                  )

angles.sort(key=lambda x: (x[1], x[2]))
destroyed_count = 0

limit = 200

while destroyed_count < limit:
    removed_angles = set()
    angles_copy = list(angles)
    for vec in angles_copy:
        if vec[1] in removed_angles:
            continue
        angles.remove(vec)
        removed_angles.add(vec[1])
        destroyed_count += 1
        if destroyed_count == limit:
            print(vec)
            break
