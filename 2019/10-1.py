#! /usr/bin/env python3

from math import tan


def calc_slope(loc_1, loc_2):
    diff = (loc_1[0] - loc_2[0], loc_1[1] - loc_2[1])
    sign_y = diff[1] / abs(diff[1]) if diff[1] else 1
    sign_x = diff[0] / abs(diff[0]) if diff[0] else 1
    return (sign_x,
            sign_y,
            (tan(diff[1] / diff[0])
             if diff[0]
             else 10000 * sign_y),
            )


with open('10-input.txt', 'r') as f:
    data = f.readlines()

# sample input
# data = """.#..#
#           .....
#           #####
#           ....#
#           ...##""".split('\n')
# data = """......#.#.
#           #..#.#....
#           ..#######.
#           .#.#.###..
#           .#..#.....
#           ..#....#.#
#           #..#....#.
#           .##.#..###
#           ##...#..#.
#           .#....####""".split('\n')
# data = """#.#...#.#.
#           .###....#.
#           .#....#...
#           ##.#.#.#.#
#           ....#.#.#.
#           .##..###.#
#           ..#...##..
#           ..##....##
#           ......#...
#           .####.###.""".split('\n')
# data = """.#..#..###
#           ####.###.#
#           ....###.#.
#           ..###.##.#
#           ##.##.#.#.
#           ....###..#
#           ..#.#..#.#
#           #..#.#.###
#           .##...##.#
#           .....#.#..""".split('\n')
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

data = [x.strip() for x in data]

asteroid_locs = [(x_idx, y_idx)
                 for y_idx, row in enumerate(data)
                 for x_idx, point in enumerate(row)
                 if point == '#']

max_slopes = 0
best = None

for asteroid in asteroid_locs:
    slopes = set()
    for other in asteroid_locs:
        if other == asteroid:
            continue
        slope = calc_slope(asteroid, other)
        slopes.add(slope)
    if len(slopes) > max_slopes:
        max_slopes = len(slopes)
        best = asteroid

print(best, max_slopes)
