#! /usr/bin/env python

import os
import sys

sys.setrecursionlimit(5000)

#read input
with open('8-input.txt','r') as f:
	content = f.read().split(' ')

content = [int(x) for x in content]

#header has two numbers exactly: # nodes, # of metadata entries.
#idea is to use recursion to calculate this

def find_subtrees(license_key,start_location=0):
	header = license_key[start_location:start_location+2] #first two numbers
	subnode_count = header[0]
	metadata_count = header[1]
	print('node header: %s, %s' % (subnode_count,metadata_count))

	if subnode_count == 0:
		# print('returning: %s %s'% (sum(license_key[2:2+metadata_count]),metadata_count+2))
		return sum(license_key[2:2+metadata_count]),metadata_count+2

	body = license_key[start_location+2:]
	metadata_sum = 0
	progress = 0

	for subnode in range(subnode_count):
		new_metadata,new_progress = find_subtrees(body,progress)
		metadata_sum += new_metadata
		progress += new_progress

	# print('in node: %s, %s' % (subnode_count,metadata_count))
	# print('body, prog: %s %s'%(body,progress))
	metadata_sum += sum(body[progress:progress+metadata_count])

	return metadata_sum,progress+2

metadata_sum,_ = find_subtrees(content)

print('total metadata: %s' % metadata_sum)
