#! /usr/bin/env python

import os
import pandas as pd
import numpy as np
import re

with open('7-input.txt','r') as f:
	content = f.read().split('\n')

#this is a Directed Acyclic Graph problem

ELF_WORKERS = 5
reqs_tuples = []

for line in content:
	match = re.search(r'Step (.) must be finished before step (.) can begin.',line)
	reqs_tuples.append((match.group(1),match.group(2)))

class Step():
	def __init__(self,name):
		self.name = name
		self.reqs = []
		self.time_required = ord(name)-64+60
		self.elapsed_time = 0
		self.done = False

	def add_time(self,s):
		self.elapsed_time +=s
		if self.elapsed_time >= self.time_required:
			self.done = True

	def add_req(self,req):
		self.reqs.append(req)

	def __repr__(self):
		temp = self.reqs
		temp.sort()
		return '; '.join(temp)

	def __str__(self):
		return self.name

class Worker():
	current_task = Step('.')
	busy = False

	def __repr__(self):
		return self.current_task.name

all_letters = set()
steps = {}

for tup in reqs_tuples:
	all_letters.update(tup)
	if tup[1] not in steps.keys():
		steps[tup[1]] = Step(tup[1])
	if tup[0] not in steps.keys():
		steps[tup[0]] = Step(tup[0])
	steps[tup[1]].add_req(tup[0])

workers = [Worker() for x in range(ELF_WORKERS)]

correct_order = set()
total_time = 0

while len(correct_order) < len(all_letters):
	potentials = []
	for letter in all_letters:
		if len(steps[letter].reqs) == 0 or all(((x in correct_order) for x in steps[letter].reqs)):
			potentials.append(letter)
	potentials.sort()

	i=0
	for worker in workers:
		try:
			if not worker.busy:
				letter = [x for x in potentials if x not in correct_order][i]
				i+=1
				if (len(steps[letter].reqs) == 0 or all(((x in correct_order) for x in steps[letter].reqs))) and (letter not in [work.current_task.name for work in workers]):
					worker.current_task = steps[letter]
					worker.busy = True
		except IndexError:
			pass

	print("\r%ss - currently working on: %s                    " % (total_time,', '.join([worker.current_task.name for worker in workers if hasattr(worker.current_task,'name')])),end='')

	total_time += 1
	
	for worker in [w for w in workers if w.busy]:
		worker.current_task.add_time(1)
		if worker.current_task.done:
			correct_order.add(worker.current_task.name)
			worker.busy = False
			worker.current_task = Step('.')

print('')
print(total_time)
