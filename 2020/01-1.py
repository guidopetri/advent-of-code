#! /usr/bin/env python3

with open('01-input.txt', 'r') as f:
    data = f.readlines()

data = list(map(int, data))
data.sort()

done = False

for idx, point in enumerate(data):
    for idx_rev, point_rev in enumerate(data[::-1]):
        if point + point_rev < 2020:
            break
        if point + point_rev == 2020:
            print(point * point_rev)
            done = True
    if done:
        break
