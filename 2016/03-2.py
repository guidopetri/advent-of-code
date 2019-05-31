#! /usr/bin/env python

import re


def valid_triangle(num1, num2, num3):
    s1 = num2 + num3
    s2 = num1 + num3
    s3 = num1 + num2

    return ((s1 > num1) & (s2 > num2) & (s3 > num3))


with open('03-input.txt', 'r') as f:
    data = f.read()

valid_triangles = 0

for lines in re.finditer(r'.+?\n.+?\n.+?\n', data):
    line_list = lines.group(0).split('\n')
    line_list = [x for x in line_list if len(x) > 1]

    line_groups = []
    for line in line_list:
        line_groups.append(re.search(r'(\d+) +(\d+) +(\d+)', line))

    triangles = [[x.group(y) for x in line_groups] for y in range(1, 4)]
    for triangle in triangles:
        first_num = int(triangle[0])
        second_num = int(triangle[1])
        third_num = int(triangle[2])

        if valid_triangle(first_num, second_num, third_num):
            valid_triangles += 1

print("Valid triangles: {}".format(valid_triangles))
