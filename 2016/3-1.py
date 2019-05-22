#! /usr/bin/env python

import os
import sys
import re

with open('3-1-input.txt','r') as f:
	data = f.read().split('\n')

valid_triangles = 0

for line in data:
	if len(line) > 3:
		numbers = re.search(r'(\d+) +(\d+) +(\d+)',line)
		first_num = int(numbers.group(1))
		second_num = int(numbers.group(2))
		third_num = int(numbers.group(3))

		if ((first_num + second_num > third_num) &
			(first_num + third_num > second_num) &
			(second_num + third_num > first_num)):
			valid_triangles += 1

print("Valid triangles: {}".format(valid_triangles))
