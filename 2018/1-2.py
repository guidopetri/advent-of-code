#! /usr/bin/env python

import os

with open('1-input.txt','r') as f:
	content = f.read().split('\n')

content = [int(x) for x in content]

frequencies = [0]

current_frequency = 0
done = False

while not done:
	for x in content:
		current_frequency +=x
		if current_frequency in frequencies:
			print('%s is the first repeat frequency' % current_frequency)
			done=True
			break
		frequencies.append(current_frequency)

print('done with program')
