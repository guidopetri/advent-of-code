#! /usr/bin/env python3

from collections import Counter

with open('06-input.txt', 'r') as f:
    data = f.read().split('\n\n')

running_sum = 0

for group in data:
    answers = group.split()

    answers_unique = Counter()
    [answers_unique.update(x) for x in answers]

    running_sum += sum([value == len(answers)
                        for value in answers_unique.values()])

print(running_sum)
