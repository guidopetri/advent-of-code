#! /usr/bin/env python3

with open('03-input.txt', 'r') as f:
    data = f.readlines()

# data = """..##.......
#           #...#...#..
#           .#....#..#.
#           ..#.#...#.#
#           .#...##..#.
#           ..#.##.....
#           .#.#.#....#
#           .#........#
#           #.##...#...
#           #...##....#
#           .#..#...#.#
#           .##########
#           ..#.#######
#           #.####.####
#           """.split()

data = [list(x.strip()) for x in data]

down_by = 1
right_by = 3
horz_len = len(data[0])
print(len(data), horz_len)

current_idx = (0, 0)

at_bottom = lambda: current_idx[0] + 1 == len(data)
trees = 0

while True:
    current_idx = (current_idx[0] + down_by,
                   (current_idx[1] + right_by) % horz_len)

    trees += data[current_idx[0]][current_idx[1]] == '#'
    if at_bottom():
        break

print(trees)
