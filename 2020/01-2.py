#! /usr/bin/env python3

with open('01-input.txt', 'r') as f:
    data = f.readlines()

data = list(map(int, data))
data.sort()

done = False

for point in data:
    for point_2 in data:
        for point_rev in data[::-1]:
            if point + point_2 + point_rev < 2020:
                break
            if point + point_2 + point_rev == 2020:
                print(point * point_2 * point_rev)
                done = True
        if done:
            break
    if done:
        break
