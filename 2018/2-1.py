#! /usr/bin/env python

import os

with open('2-input.txt','r') as f:
	content = f.read().split('\n')

two_letter_count = 0
three_letter_count = 0

for box in content:
	counts = {x:box.count(x) for x in box}
	if 2 in counts.values():
		two_letter_count+=1
	if 3 in counts.values():
		three_letter_count+=1

print(two_letter_count*three_letter_count)
