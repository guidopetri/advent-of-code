#! /usr/bin/env python3

with open('06-input.txt', 'r') as f:
    data = f.read().split('\n\n')

running_sum = 0

for group in data:
    answers = group.split()

    answers_unique = set()
    [answers_unique.update(x) for x in answers]

    running_sum += len(answers_unique)

print(running_sum)
