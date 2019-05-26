#! /usr/bin/env python

with open('1-input.txt', 'r') as f:
    content = f.read().split('\n')

content = [int(x) for x in content]
print(sum(content))
