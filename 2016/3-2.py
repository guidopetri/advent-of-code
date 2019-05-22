#! /usr/bin/env python

import os
import sys
import re

with open('3-1-input.txt','r') as f:
	data = f.read()

valid_triangles = 0

for lines in re.finditer(r'.+?\n.+?\n.+?\n',data):
	line_list = lines.group(0).split('\n')
	line_list = [x for x in line_list if len(x) > 1]
	line_groups = [re.search(r'(\d+) +(\d+) +(\d+)',line) for line in line_list]
	triangles = [[x.group(y) for x in line_groups] for y in range(1,4)]
	for triangle in triangles:
		first_num = int(triangle[0])
		second_num = int(triangle[1])
		third_num = int(triangle[2])
		if ((first_num + second_num > third_num) &
			(first_num + third_num > second_num) &
			(second_num + third_num > first_num)):
			valid_triangles += 1

print("Valid triangles: {}".format(valid_triangles))
