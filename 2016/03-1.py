#! /usr/bin/env python

import re


def valid_triangle(num1, num2, num3):
    s1 = num2 + num3
    s2 = num1 + num3
    s3 = num1 + num2

    return ((s1 > num1) & (s2 > num2) & (s3 > num3))


with open('3-1-input.txt', 'r') as f:
    data = f.read().split('\n')

valid_triangles = 0

for line in data:
    if len(line) > 3:
        numbers = re.search(r'(\d+) +(\d+) +(\d+)', line)
        first_num = int(numbers.group(1))
        second_num = int(numbers.group(2))
        third_num = int(numbers.group(3))

        if valid_triangle(first_num, second_num, third_num):
            valid_triangles += 1

print("Valid triangles: {}".format(valid_triangles))
